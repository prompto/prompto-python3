from prompto.error.InvalidDataError import InvalidDataError
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.BooleanType import BooleanType
from prompto.value.Boolean import Boolean


class WhileStatement ( BaseStatement ):

    def __init__(self, condition, instructions):
        super(WhileStatement, self).__init__()
        self.condition = condition
        self.instructions = instructions

    def getCondition(self):
        return self.condition

    def getInstructions(self):
        return self.instructions

    def check(self, context):
        cond = self.condition.check(context)
        if cond!=BooleanType.instance:
            raise SyntaxError("Expected a Boolean condition!")
        child = context.newChildContext()
        return self.instructions.check(child, None)

    def interpret(self, context):
        while self.interpretCondition(context):
            child = context.newChildContext()
            value = self.instructions.interpret(child)
            if value is not None:
                return value
        return None

    def interpretCondition(self, context):
        value = self.condition.interpret(context)
        if not isinstance(value, Boolean):
            raise InvalidDataError("Expected a Boolean, got:" + type(value).__name__)
        return value.value

    def toEDialect(self, writer):
        writer.append("while ")
        self.condition.toDialect(writer)
        writer.append(" :\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        writer.append("while (")
        self.condition.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        writer.append("}\n")

    def toSDialect(self, writer):
        self.toEDialect(writer)


