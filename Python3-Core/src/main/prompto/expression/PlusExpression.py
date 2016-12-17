from prompto.expression.IExpression import IExpression

class PlusExpression(IExpression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " + " + str(self.right)

    def toDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(" + ")
        self.right.toDialect(writer)

    def check(self, context):
        lt = self.left.check(context)
        rt = self.right.check(context)
        return lt.checkAdd(context, rt, True)

    def interpret(self, context):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        return lval.Add(context, rval)