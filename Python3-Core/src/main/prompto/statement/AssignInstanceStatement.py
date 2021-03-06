from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.CodeType import CodeType
from prompto.type.VoidType import VoidType


class AssignInstanceStatement ( SimpleStatement ):

    def __init__(self, instance, expression):
        super(AssignInstanceStatement, self).__init__()
        self.instance = instance
        self.expression = expression

    def __str__(self):
        return str(self.instance) + " = " + str(self.expression)

    def toDialect(self, writer):
        self.instance.toDialect(writer, self.expression)
        writer.append(" = ")
        self.expression.toDialect(writer)

    def getExpression(self):
        return self.expression

    def check(self, context):
        valueType = self.expression.check(context)
        self.instance.checkAssignValue(context, valueType)
        # Code expressions need to be interpreted as part of full check
        if valueType is CodeType.instance:
            self.instance.assign(context, self.expression)
        return VoidType.instance

    def interpret(self, context):
        self.instance.assign(context,self.expression)
        return None
