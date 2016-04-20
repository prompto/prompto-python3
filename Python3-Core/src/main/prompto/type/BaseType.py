from prompto.type.IType import IType
from prompto.expression.IExpression import IExpression
from prompto.value.ExpressionValue import ExpressionValue
from prompto.value.ListValue import ListValue
from prompto.error.SyntaxError import SyntaxError

class BaseType(IType):

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __eq__(self, obj):
        if obj is None:
            return False
        if id(self) == id(obj):
            return True
        if not isinstance(obj, IType):
            return False
        return self.getName() == obj.getName()

    def __ne__(self, obj):
        return not self == obj

    def __str__(self):
        return self.name

    def toDialect(self, writer):
        writer.append(self.getName())

    def checkAdd(self, context, other, tryReverse):
        if tryReverse:
            return other.checkAdd(context, self, False)
        else:
            raise SyntaxError("Cannot add " + self.getName() + " to " + other.getName())

    def checkSubstract(self, context, other):
        raise SyntaxError("Cannot substract " + self.getName() + " from " + other.getName())

    def checkDivide(self, context, other):
        raise SyntaxError("Cannot divide " + self.getName() + " with " + other.getName())

    def checkIntDivide(self, context, other):
        raise SyntaxError("Cannot int_divide " + self.getName() + " with " + other.getName())

    def checkModulo(self, context, other):
        raise SyntaxError("Cannot modulo " + self.getName() + " with " + other.getName())

    def checkMultiply(self, context, other, tryReverse):
        if tryReverse:
            return other.checkMultiply(context, self, False)
        else:
            raise SyntaxError("Cannot multiply " + self.getName() + " with " + other.getName())

    def checkCompare(self, context, other):
        raise SyntaxError("Cannot compare " + self.getName() + " to " + other.getName())

    def checkContains(self, context, other):
        raise SyntaxError(self.getName() + " cannot contain " + other.getName())

    def checkContainsAllOrAny(self, context, other):
        raise SyntaxError(self.getName() + " cannot contain " + other.getName())

    def checkItem(self, context, itemType):
        raise SyntaxError("Cannot read item from " + self.getName())

    def checkMember(self, context, name):
        raise SyntaxError("Cannot read member from " + self.getName())

    def checkSlice(self, context):
        raise SyntaxError("Cannot slice " + self.getName())

    def checkIterator(self, context):
        raise SyntaxError("Cannot iterate over " + self.getName())

    def checkAssignableTo(self, context, other):
        if not self.isAssignableTo(context, other):
            raise SyntaxError("Type: " + self.getName() + " is not compatible with: " + other.getName())

    def checkRange(self, context, other):
        raise SyntaxError("Cannot create range of " + self.getName() + " and " + other.getName())

    def newRange(self, left, right):
        raise SyntaxError("Cannot create range of " + self.getName())

    def toString(self, value):
        return str(value)

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        raise Exception("Unsupported!")

    def sort(self, context, source, key=None):
        raise Exception("Unsupported!")

    def readJSONValue(self, context, node, parts):
        raise Exception("Unsupported!")
