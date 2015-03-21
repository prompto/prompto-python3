import threading

from presto.grammar.Operator import Operator
from presto.type.DecimalType import DecimalType
from presto.value.Decimal import Decimal
from presto.value.Integer import Integer
from presto.value.IInstance import IInstance
from presto.value.IMultiplyable import IMultiplyable
from presto.declaration.AttributeDeclaration import AttributeDeclaration
from presto.value.ContextualExpression import *
from presto.value.ExpressionValue import *
from presto.value.Dictionary import Dictionary
from presto.runtime.Variable import Variable
from presto.error.SyntaxError import SyntaxError

# don't call getters from getters, so register them
activeGetters = threading.local()
# don't call setters from setters, so register them
activeSetters = threading.local()


class ConcreteInstance(BaseValue, IInstance, IMultiplyable):

    def __init__(self, declaration):
        from presto.type.CategoryType import CategoryType
        super(ConcreteInstance, self).__init__(CategoryType(declaration.name))
        self.declaration = declaration
        self.values = dict()

    def getDeclaration(self):
        return self.declaration

    def getType(self):
        from presto.type.CategoryType import CategoryType
        return CategoryType(self.declaration.getName())

    def getAttributeNames(self):
        return self.values.keys()

    def getMember(self, context, attrName):
        stacked = activeGetters.__dict__.get(attrName, None)
        try:
            return self.get(context, attrName, stacked == None)
        finally:
            if stacked == context:
                del activeGetters.__dict__[attrName]

    def get(self, context, attrName, allowGetter):
        getter = self.declaration.findGetter(context, attrName) if allowGetter else None
        if getter != None:
            activeGetters.__dict__[attrName] = context
            context = context.newInstanceContext(self, None)
            return ContextualExpression(context, getter)
        else:
            return self.values.get(attrName, None)

    def set(self, context, attrName, value):
        stacked = activeSetters.__dict__.get(attrName, None)
        try:
            self.doSet(context, attrName, value, stacked == None)
        finally:
            if stacked == context:
                del activeSetters.__dict__[attrName]

    def doSet(self, context, attrName, value, allowSetter):
        decl = context.getRegisteredDeclaration(AttributeDeclaration, attrName)
        setter = self.declaration.findSetter(context, attrName) if allowSetter else None
        if setter != None:
            activeSetters.__dict__[attrName] = context
            # use attribute name as parameter name for incoming value
            context = context.newInstanceContext(self, None)
            context.registerValue(Variable(attrName, decl.getType()))
            context.setValue(attrName, value)
            value = setter.interpret(context)
        value = self.autocast(decl, value)
        self.values[attrName] = value

    def autocast(self, decl, value):
        if isinstance(value, Integer) and decl.getType() is DecimalType.instance:
            value = Decimal(value.DecimalValue())
        return value

    def __eq__(self, obj):
        if not isinstance(obj, ConcreteInstance):
            return False
        return self.values == obj.values

    def __str__(self):
        return str(Dictionary(MissingType.instance, value=self.values))

    def __hash__(self):
        return hash((self.declaration.name,frozenset(self.values.items())))
    
    def Multiply(self, context, value):
        try:
            return self.interpretOperator(context, value, Operator.MULTIPLY)
        except SyntaxError as e:
            return super().Multiply(context, value)


    def Divide(self, context, value):
        try:
            return self.interpretOperator(context, value, Operator.DIVIDE)
        except SyntaxError as e:
            return super().Divide(context, value)


    def IntDivide(self, context, value):
        try:
            return self.interpretOperator(context, value, Operator.IDIVIDE)
        except SyntaxError as e:
            return super().IntDivide(context, value)


    def Modulo(self, context, value):
        try:
            return self.interpretOperator(context, value, Operator.MODULO)
        except SyntaxError as e:
            return super().Modulo(context, value)


    def Add(self, context, value):
        try:
            return self.interpretOperator(context, value, Operator.PLUS)
        except SyntaxError as e:
            return super().Add(context, value)


    def Subtract(self, context, value):
        try:
            return self.interpretOperator(context, value, Operator.MINUS)
        except SyntaxError as e:
            return super().Subtract(context, value)


    def interpretOperator(self, context, value, operator):
        decl = self.declaration.findOperator(context, operator, value.type)
        context = context.newInstanceContext(self, None)
        local = context.newChildContext()
        decl.registerArguments(local)
        arg = decl.arguments[0]
        local.setValue(arg.name, value)
        return decl.interpret(local)
