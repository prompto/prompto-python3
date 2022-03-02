from prompto.declaration.IDeclaration import IDeclaration
from prompto.expression.IExpression import IExpression
from prompto.error.SyntaxError import SyntaxError
from prompto.runtime.Context import MethodDeclarationMap
from prompto.type.AnyType import AnyType
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.type.IterableType import IterableType
from prompto.type.MethodType import MethodType
from prompto.type.NativeType import NativeType
from prompto.value.DecimalValue import DecimalValue
from prompto.value.IntegerValue import IntegerValue
from prompto.value.NullValue import NullValue


def getTargetType(context, itype, mutable):
    if isinstance(itype, IterableType):
        itemType = getTargetType(context, itype.itemType, False)
        return itype.withItemType(itemType).asMutable(context, mutable)
    elif isinstance(itype, NativeType):
        return itype.asMutable(context, mutable)
    else:
        return getTargetAtomicType(context, itype).asMutable(context, mutable)


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


    def __init__(self, expression, itype, mutable):
        self.expression = expression
        self.itype = itype.anyfy()
        self.mutable = mutable


    def check(self, context):
        actual = self.expression.check(context).anyfy()
        target = getTargetType(context, self.itype, self.mutable)
        if actual == target:
            return target
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
        if value is not None and value != NullValue.instance:
            target = getTargetType(context, self.itype, self.mutable)
            if target != value.itype:
                if isinstance(value, IntegerValue) and target == DecimalType.instance:
                    value = DecimalValue(value.DecimalValue())
                elif isinstance(value, DecimalValue) and target == IntegerType.instance:
                    return IntegerValue(value.IntegerValue())
                elif value.itype.isAssignableFrom(context, target):
                    value.itype = self.itype
                elif not target.isAssignableFrom(context, value.itype):
                    raise SyntaxError("Cannot cast " + str(value.itype) + " to " + str(self.itype))
        return value


    def toMDialect(self, writer):
        self.toEDialect(writer)


    def toEDialect(self, writer):
        self.expression.toDialect(writer)
        writer.append(" as ")
        if self.mutable:
            writer.append("mutable ")
        self.itype.toDialect(writer)


    def toODialect(self, writer):
        writer.append("(")
        if self.mutable:
            writer.append("mutable ")
        self.itype.toDialect(writer)
        writer.append(")")
        self.expression.toDialect(writer)

