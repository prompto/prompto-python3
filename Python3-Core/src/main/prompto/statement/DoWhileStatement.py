from prompto.error.InvalidDataError import InvalidDataError
from prompto.runtime.BreakResult import BreakResult
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.BooleanType import BooleanType
from prompto.value.Boolean import Boolean


class DoWhileStatement ( BaseStatement ):

    def __init__(self, condition, instructions):
        super().__init__()
        self.condition = condition
        self.instructions = instructions

    def check(self, context):
        cond = self.condition.check(context)
        if cond!=BooleanType.instance:
            raise SyntaxError("Expected a Boolean condition!")
        child = context.newChildContext()
        return self.instructions.check(child, None)

    def interpret(self, context):
        while True:
            child = context.newChildContext()
            value = self.instructions.interpret(child)
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
            raise InvalidDataError("Expected a Boolean, got:" + type(value).__name__)
        return value.value

    def toEDialect(self, writer):
        writer.append("do:\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        writer.append("while ")
        self.condition.toDialect(writer)
        writer.newLine()

    def toODialect(self, writer):
        writer.append("do {\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        writer.append("} while (")
        self.condition.toDialect(writer)
        writer.append(");\n")

    def toSDialect(self, writer):
        self.toEDialect(writer)
