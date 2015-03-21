from presto.expression.IExpression import IExpression


class IntDivideExpression ( IExpression ):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return self.left.toString() + " \\ " + self.right.toString()

    def toDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(" \\ ")
        self.right.toDialect(writer)

    def check(self, context):
        lt = self.left.check(context)
        rt = self.right.check(context)
        return lt.checkIntDivide(context, rt)

    def interpret(self, context):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        return lval.IntDivide(context, rval)
