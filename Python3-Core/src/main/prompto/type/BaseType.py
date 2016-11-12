from prompto.type.IType import IType
from prompto.expression.IExpression import IExpression
from prompto.value.ExpressionValue import ExpressionValue
from prompto.error.SyntaxError import SyntaxError

class BaseType(IType):

    def __init__(self, family):
        self.family = family
        self.typeName = str(family)[len("TypeFamily."):].capitalize()


    def __eq__(self, obj):
        if obj is None:
            return False
        if id(self) == id(obj):
            return True
        if isinstance(obj, IType):
            return self.typeName == obj.typeName
        else:
            return False


    def __ne__(self, obj):
        return not self == obj

    def __str__(self):
        return self.typeName


    def toDialect(self, writer):
        writer.append(self.typeName)


    def checkAdd(self, context, other, tryReverse):
        if tryReverse:
            return other.checkAdd(context, self, False)
        else:
            raise SyntaxError("Cannot add " + self.typeName + " to " + other.typeName)


    def checkSubstract(self, context, other):
        raise SyntaxError("Cannot substract " + self.typeName + " from " + other.typeName)


    def checkDivide(self, context, other):
        raise SyntaxError("Cannot divide " + self.typeName + " with " + other.typeName)


    def checkIntDivide(self, context, other):
        raise SyntaxError("Cannot int_divide " + self.typeName + " with " + other.typeName)


    def checkModulo(self, context, other):
        raise SyntaxError("Cannot modulo " + self.typeName + " with " + other.typeName)


    def checkMultiply(self, context, other, tryReverse):
        if tryReverse:
            return other.checkMultiply(context, self, False)
        else:
            raise SyntaxError("Cannot multiply " + self.typeName + " with " + other.typeName)


    def checkCompare(self, context, other):
        raise SyntaxError("Cannot compare " + self.typeName + " to " + other.typeName)


    def checkContains(self, context, other):
        raise SyntaxError(self.typeName + " cannot contain " + other.typeName)


    def checkContainsAllOrAny(self, context, other):
        raise SyntaxError(self.typeName + " cannot contain " + other.typeName)


    def checkItem(self, context, itemType):
        raise SyntaxError("Cannot read item from " + self.typeName)


    def checkMember(self, context, name):
        raise SyntaxError("Cannot read member from " + self.typeName)


    def checkSlice(self, context):
        raise SyntaxError("Cannot slice " + self.typeName)


    def checkIterator(self, context):
        raise SyntaxError("Cannot iterate over " + self.typeName)


    def checkRange(self, context, other):
        raise SyntaxError("Cannot create range of " + self.typeName + " and " + other.typeName)



    def newRange(self, left, right):
        raise SyntaxError("Cannot create range of " + self.typeName)



    def toString(self, value):
        return str(value)



    def convertPythonValueToPromptoValue(self, context, value, returnType):
        raise Exception("Unsupported!")



    def sort(self, context, source, desc, key=None):
        raise Exception("Unsupported!")



    def readJSONValue(self, context, node, parts):
        raise Exception("Unsupported!")



    def isAssignableFrom(self, context, other:IType):
        from prompto.type.NullType import NullType
        return other is NullType.instance \
            or self is other \
            or self == other \
            or self.typeName == other.typeName



    def checkAssignableFrom(self, context, other):
        if not self.isAssignableFrom(context, other):
            raise SyntaxError("Type: " + self.typeName + " is not compatible with: " + other.typeName)


