import threading
from io import StringIO

from prompto.error.NotStorableError import NotStorableError
from prompto.grammar.Operator import Operator
from prompto.store.DataStore import DataStore
from prompto.type.DecimalType import DecimalType
from prompto.utils.TypeUtils import fieldToValue
from prompto.value.Decimal import Decimal
from prompto.value.Integer import Integer
from prompto.value.IInstance import IInstance
from prompto.value.IMultiplyable import IMultiplyable
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.value.ExpressionValue import *
from prompto.runtime.Variable import Variable
from prompto.error.SyntaxError import SyntaxError
from prompto.error.NotMutableError import NotMutableError

# don't call getters from getters, so register them
activeGetters = threading.local()
# don't call setters from setters, so register them
activeSetters = threading.local()


class ConcreteInstance(BaseValue, IInstance, IMultiplyable):

    def __init__(self, context, declaration):
        from prompto.type.CategoryType import CategoryType
        super(ConcreteInstance, self).__init__(CategoryType(declaration.name))
        self.declaration = declaration
        self.storable = None
        if declaration.storable:
            categories = declaration.collectCategories(context)
            self.storable = DataStore.instance.newStorable(categories)
        self.mutable = False
        self.values = dict()

    def getDeclaration(self):
        return self.declaration

    def getType(self):
        from prompto.type.CategoryType import CategoryType
        return CategoryType(self.declaration.getName())


    def getDbId(self):
        dbId = self.values.get("dbId", None)
        return None if dbId is None else dbId.getStorableData()


    def getOrCreateDbId(self):
        dbId = self.getDbId()
        if dbId is None:
            dbId = self.storable.getOrCreateDbId()
            value = fieldToValue(None, "dbId", dbId)
            self.values["dbId"] = value
        return dbId


    def getStorableData(self):
        # this is called when storing the instance as a field value, so we just return the dbId
        # the instance data itself will be collected as part of collectStorables
        if self.storable is None:
            raise NotStorableError()
        else:
            return self.getOrCreateDbId()


    def collectStorables(self, list):
        if self.storable is None:
            raise NotStorableError()
        if self.storable.dirty:
            self.getOrCreateDbId()
            list.append(self.storable)
        for value in self.values.values():
            value.collectStorables(list)


    def getMemberNames(self):
        return self.values.keys()

    def getMemberValue(self, context, attrName, autoCreate=False):
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
        if getter is not None:
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
        if setter is not None:
            activeSetters.__dict__[attrName] = context
            # use attribute name as parameter name for incoming value
            context = context.newInstanceContext(self, None).newChildContext()
            context.registerValue(Variable(attrName, decl.getType()))
            context.setValue(attrName, value)
            value = setter.interpret(context)
        value = self.autocast(decl, value)
        self.values[attrName] = value
        if self.storable is not None and decl.storable:
            # TODO convert object graph if(value instanceof IInstance)
            self.storable.setData(attrName, value.getStorableData())


    def autocast(self, decl, value):
        if isinstance(value, Integer) and decl.getType() is DecimalType.instance:
            value = Decimal(value.DecimalValue())
        return value

    def __eq__(self, obj):
        if not isinstance(obj, ConcreteInstance):
            return False
        return self.values == obj.values

    def __str__(self):
        with StringIO() as sb:
            sb.write(u"{")
            for k, v in self.values.items():
                if "dbId"==k:
                    continue
                sb.write(str(k))
                sb.write(u":")
                sb.write(str(v))
                sb.write(u", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len - 2)
                sb.truncate(len - 2)
            sb.write(u"}")
            return sb.getvalue()


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
        decl = self.declaration.getOperatorMethod(context, operator, value.type)
        context = context.newInstanceContext(self, None)
        local = context.newChildContext()
        decl.registerArguments(local)
        arg = decl.arguments[0]
        local.setValue(arg.name, value)
        return decl.interpret(local)
