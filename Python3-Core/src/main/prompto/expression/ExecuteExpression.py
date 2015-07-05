from prompto.error.PrestoError import PrestoError
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.CodeExpression import CodeExpression
from prompto.expression.IExpression import IExpression
from prompto.parser.ISection import ISection
from prompto.parser.Section import Section
from prompto.value.CodeValue import CodeValue

class ExecuteExpression ( Section, IExpression, ISection ):

    def __init__(self, name):
        super(ExecuteExpression, self).__init__()
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return "execute: " + self.name

    def toSDialect(self, writer):
        writer.append("execute(")
        writer.append(self.name)
        writer.append(")")

    def toEDialect(self, writer):
        writer.append("execute: ")
        writer.append(self.name)

    def toODialect(self, writer):
        writer.append("execute(")
        writer.append(self.name)
        writer.append(")")

    def check(self, context):
        try:
            value = context.getValue(self.name)
            if isinstance(value, CodeValue):
                return value.check(context)
            else:
                raise SyntaxError("Expected code, got:" + str(value))
        except PrestoError as e:
            raise SyntaxError(e.getMessage())

    def interpret(self, context):
        value = context.getValue(self.name)
        if isinstance(value, CodeValue):
            return value.interpret(context)
        else:
            raise SyntaxError("Expected code, got:" + value.toString())
