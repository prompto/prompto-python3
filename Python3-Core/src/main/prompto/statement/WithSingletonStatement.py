from prompto.statement.BaseStatement import BaseStatement
from prompto.statement.SimpleStatement import SimpleStatement

class WithSingletonStatement(BaseStatement):

    def __init__(self, type, instructions):
        super().__init__()
        self.type = type
        self.instructions = instructions

    def check(self, context):
        instanceContext = context.newInstanceContext(None, self.type, True)
        childContext = instanceContext.newChildContext()
        return self.instructions.check(childContext, None)

    def interpret(self, context):
        # TODO synchronize
        instance = context.loadSingleton(self.type)
        instanceContext = context.newInstanceContext(instance, None, True)
        childContext = instanceContext.newChildContext()
        return self.instructions.interpret(childContext)

    def toEDialect(self, writer):
        writer.append("with ")
        self.type.toDialect(writer)
        writer.append(", do:\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        writer.append("with (")
        self.type.toDialect(writer)
        writer.append(")")
        oneLine = len(self.instructions)==1 and self.instructions[0].isSimple()
        if not oneLine:
            writer.append(" {")
        writer.newLine()
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        if not oneLine:
            writer.append("}")
            writer.newLine()

    def toMDialect(self, writer):
        writer.append("with ")
        self.type.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
