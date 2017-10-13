from prompto.error.UserError import UserError
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.CategoryType import CategoryType
from prompto.type.VoidType import VoidType
from prompto.error.SyntaxError import SyntaxError

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

    def toMDialect(self, writer):
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
        itype = self.expression.check(context)
        if not CategoryType("Error").isAssignableFrom(context, itype):
            raise SyntaxError(itype.getName() + " does not extend Error")
        return VoidType.instance

    def interpret(self, context):
        raise UserError(self.expression)
