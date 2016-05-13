import threading

from prompto.grammar.Operator import Operator
from prompto.type.DecimalType import DecimalType
from prompto.value.Decimal import Decimal
from prompto.value.Integer import Integer
from prompto.value.IInstance import IInstance
from prompto.value.IMultiplyable import IMultiplyable
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.value.ContextualExpression import *
from prompto.value.ExpressionValue import *
from prompto.value.Dictionary import Dictionary
from prompto.runtime.Variable import Variable
from prompto.error.SyntaxError import SyntaxError
from prompto.error.NotMutableError import NotMutableError
from prompto.store.StorableDocument import StorableDocument

# don't call getters from getters, so register them
activeGetters = threading.local()
# don't call setters from setters, so register them
activeSetters = threading.local()


class ConcreteInstance(BaseValue, IInstance, IMultiplyable):

    def __init__(self, declaration):
        from prompto.type.CategoryType import CategoryType
        super(ConcreteInstance, self).__init__(CategoryType(declaration.name))
        self.declaration = declaration
        self.storable = StorableDocument() if declaration.storable else None
        self.mutable = False
        self.values = dict()

    def getDeclaration(self):
        return self.declaration

    def getType(self):
        from prompto.type.CategoryType import CategoryType
        return CategoryType(self.declaration.getName())

    def getMemberNames(self):
        return self.values.keys()

    def getMember(self, context, attrName, autoCreate=False):
        stacked = activeGetters.__dict__.get(attrName, None)
        first = stacked is None
        if first:
            activeGetters.__dict__[attrName] = context
        try:
            return self.doGetMember(context, attrName, first)
        finally:
            if first:
                del activeGetters.__dict__[attrName]

    def doGetMember(self, context, attrName, allowGetter):
        getter = self.declaration.findGetter(context, attrName) if allowGetter else None
        if getter != None:
            context = context.newInstanceContext(self, None).newChildContext()
            return getter.interpret(context)
        else:
            return self.values.get(attrName, None)

    def setMember(self, context, attrName, value):
        if not self.mutable:
            raise NotMutableError()
        stacked = activeSetters.__dict__.get(attrName, None)
        first = stacked is None
        if first:
            activeSetters.__dict__[attrName] = context
        try:
            self.doSetMember(context, attrName, value, first)
        finally:
            if first:
                del activeSetters.__dict__[attrName]


    def doSetMember(self, context, attrName, value, allowSetter):
        decl = context.getRegisteredDeclaration(AttributeDeclaration, attrName)
        setter = self.declaration.findSetter(context, attrName) if allowSetter else None
        if setter != None:
            activeSetters.__dict__[attrName] = context
            # use attribute name as parameter name for incoming value
            context = context.newInstanceContext(self, None).newChildContext()
            context.registerValue(Variable(attrName, decl.getType()))
            context.setValue(attrName, value)
            value = setter.interpret(context)
        value = self.autocast(decl, value)
        self.values[attrName] = value
        if self.storable is not None:
            if decl.storable:
                # TODO convert object graph if(value instanceof IInstance)
                self.storable.SetMember(context, attrName, value)


    def autocast(self, decl, value):
        if isinstance(value, Integer) and decl.getType() is DecimalType.instance:
            value = Decimal(value.DecimalValue())
        return value

    def __eq__(self, obj):
        if not isinstance(obj, ConcreteInstance):
            return False
        return self.values == obj.values

    def __str__(self):
        return str(Dictionary(MissingType.instance, False, value=self.values))

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
