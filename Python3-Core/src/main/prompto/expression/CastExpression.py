from prompto.declaration.IDeclaration import IDeclaration
from prompto.expression.IExpression import IExpression
from prompto.error.SyntaxError import SyntaxError
from prompto.runtime.Context import MethodDeclarationMap
from prompto.type.AnyType import AnyType
from prompto.type.CategoryType import CategoryType
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.type.IterableType import IterableType
from prompto.type.MethodType import MethodType
from prompto.type.NativeType import NativeType
from prompto.value.Decimal import Decimal
from prompto.value.Integer import Integer


def getTargetType(context, itype):
    if isinstance(itype, IterableType):
        itemType = getTargetType(context, itype.itemType)
        return itype.withItemType(itemType)
    elif isinstance(itype, NativeType):
        return itype
    else:
        return getTargetAtomicType(context, itype)


def getTargetAtomicType(context, itype):
    decl = context.getRegisteredDeclaration(IDeclaration, itype.typeName)
    if decl is None:
        raise SyntaxError("Unknown identifier: " + itype.typeName)
    elif isinstance(decl, MethodDeclarationMap):
        if len(decl) == 1:
            return MethodType(decl.getFirst())
        else:
            raise SyntaxError("Ambiguous identifier: " + itype.typeName)
    else:
        return decl.getType(context)


class CastExpression (IExpression):


    def __init__(self, expression, itype):
        self.expression = expression
        self.itype = itype.anyfy()


    def check(self, context):
        actual = self.expression.check(context).anyfy()
        target = getTargetType(context, self.itype)
        # check any
        if actual == AnyType.instance:
            return target
        # check upcast
        if target.isAssignableFrom(context, actual):
            return target
        # check downcast
        if actual.isAssignableFrom(context, target):
            return target
        raise SyntaxError("Cannot cast " + str(actual) + " to " + str(target))



    def interpret(self, context):
        value = self.expression.interpret(context)
        if value is not None:
            target = getTargetType(context, self.itype)
            if isinstance(value, Integer) and target == DecimalType.instance:
                value = Decimal(value.DecimalValue())
            elif isinstance(value, Decimal) and target == IntegerType.instance:
                return Integer(value.IntegerValue())
            elif target.isMoreSpecificThan(context, value.itype):
                value.itype = self.itype
        return value

    def toMDialect(self, writer):
        self.toEDialect(writer)

    def toEDialect(self, writer):
        self.expression.toDialect(writer)
        writer.append(" as ")
        self.itype.toDialect(writer)

    def toODialect(self, writer):
        writer.append("(")
        self.itype.toDialect(writer)
        writer.append(")")
        self.expression.toDialect(writer)

