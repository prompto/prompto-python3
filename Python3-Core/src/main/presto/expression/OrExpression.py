from presto.expression.IExpression import IExpression
from presto.type.BooleanType import BooleanType
from presto.value.Boolean import Boolean
from presto.error.SyntaxError import SyntaxError

class OrExpression ( IExpression ):

    def __init__(self, left, right):
        self.left = left
        self.right = right


    def __str__(self):
        return str(self.left) + " or " + str(self.right)

    def toPDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(" or ")
        self.right.toDialect(writer)

    def toEDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(" or ")
        self.right.toDialect(writer)

    def toODialect(self, writer):
        self.left.toDialect(writer)
        writer.append(" || ")
        self.right.toDialect(writer)

    def check(self, context):
        lt = self.left.check(context)
        rt = self.right.check(context)
        if not isinstance(lt, BooleanType) or not isinstance(rt, BooleanType):
            raise SyntaxError("Cannot combine " + lt.getName() + " and " + rt.getName())
        return BooleanType.instance

    def interpret(self, context):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        if isinstance(lval, Boolean):
            if isinstance(rval, Boolean):
                return Boolean.ValueOf(lval.getValue() or rval.getValue())
            else:
                raise SyntaxError("Illegal: Boolean and " + type(rval).__name__)
        else:
            raise SyntaxError("Illegal: " + type(lval).__name__ + " + " + type(rval).__name__)
