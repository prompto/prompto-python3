from prompto.store.InvalidValueError import InvalidValueError
from prompto.runtime.BreakResult import BreakResult
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.BooleanType import BooleanType
from prompto.value.Boolean import Boolean


class DoWhileStatement ( BaseStatement ):

    def __init__(self, condition, statements):
        super().__init__()
        self.condition = condition
        self.statements = statements

    def check(self, context):
        cond = self.condition.check(context)
        if cond!=BooleanType.instance:
            raise SyntaxError("Expected a Boolean condition!")
        child = context.newChildContext()
        return self.statements.check(child, None)

    def interpret(self, context):
        while True:
            child = context.newChildContext()
            value = self.statements.interpret(child)
            if value is BreakResult.instance:
                break
            if value is not None:
                return value
            if not self.interpretCondition(context):
                return None
        return None

    def interpretCondition(self, context):
        value = self.condition.interpret(context)
        if not isinstance(value, Boolean):
            raise InvalidValueError("Expected a Boolean, got:" + type(value).__name__)
        return value.value

    def toEDialect(self, writer):
        writer.append("do:\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("while ")
        self.condition.toDialect(writer)
        writer.newLine()

    def toODialect(self, writer):
        writer.append("do {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("} while (")
        self.condition.toDialect(writer)
        writer.append(");\n")

    def toMDialect(self, writer):
        self.toEDialect(writer)

    def canReturn(self):
        return True