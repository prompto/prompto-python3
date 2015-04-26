from presto.error.UserError import UserError
from presto.statement.SimpleStatement import SimpleStatement
from presto.type.CategoryType import CategoryType


class RaiseStatement ( SimpleStatement ):

    def __init__(self, expression):
        self.expression = expression

    def getExpression(self):
        return self.expression

    def __str__(self):
        return "raise " + self.expression.toString()

    def toEDialect(self, writer):
        writer.append("raise ")
        self.expression.toDialect(writer)

    def toODialect(self, writer):
        writer.append("throw ")
        self.expression.toDialect(writer)

    def toSDialect(self, writer):
        writer.append("raise ")
        self.expression.toDialect(writer)

    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, RaiseStatement):
            return False
        return self.getExpression()==obj.getExpression()

    def check(self, context):
        type_ = self.expression.check(context)
        if not type_.isAssignableTo(context, CategoryType("Error")):
            raise SyntaxError(type_.getName() + " does not extend Error")
        return type_

    def interpret(self, context):
        raise UserError(self.expression)
