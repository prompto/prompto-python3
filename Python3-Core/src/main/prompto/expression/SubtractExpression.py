from prompto.expression.IExpression import IExpression
from prompto.value.IValue import IValue
from prompto.error.SyntaxError import SyntaxError

class SubtractExpression ( IExpression ):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " - " + str(self.right)

    def toDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(" - ")
        self.right.toDialect(writer)

    def check(self, context):
        lt = self.left.check(context)
        rt = self.right.check(context)
        return lt.checkSubstract(context,rt)

    def interpret(self, context):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        if isinstance(lval, IValue) and isinstance(rval, IValue):
            return lval.Subtract(context, rval)
        else:
            raise SyntaxError("Illegal: " + type(lval).__name__ + " - " + type(rval).__name__)
