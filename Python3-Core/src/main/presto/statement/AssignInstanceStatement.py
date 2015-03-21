from presto.statement.SimpleStatement import SimpleStatement
from presto.type.VoidType import VoidType


class AssignInstanceStatement ( SimpleStatement ):

    def __init__(self, instance, expression):
        super(AssignInstanceStatement, self).__init__()
        self.instance = instance
        self.expression = expression

    def __str__(self):
        return str(self.instance) + " = " + str(self.expression)

    def toDialect(self, writer):
        self.instance.toDialect(writer)
        writer.append(" = ")
        self.expression.toDialect(writer)

    def getExpression(self):
        return self.expression

    def check(self, context):
        self.instance.checkAssignValue(context, self.expression)
        return VoidType.instance

    def interpret(self, context):
        self.instance.assign(context,self.expression)
        return None
