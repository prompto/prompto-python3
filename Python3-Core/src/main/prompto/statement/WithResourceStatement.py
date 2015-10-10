from prompto.statement.BaseStatement import BaseStatement
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.value.IResource import IResource


class WithResourceStatement ( BaseStatement ):

    def __init__(self, resource, instructions):
        super(WithResourceStatement, self).__init__()
        self.resource = resource
        self.instructions = instructions

    def check(self, context):
        context = context.newResourceContext()
        self.resource.checkResource(context)
        return self.instructions.check(context, None)

    def interpret(self, context):
        context = context.newResourceContext()
        try:
            self.resource.interpret(context)
            return self.instructions.interpret(context)
        finally:
            res = context.getValue(self.resource.getName())
            if isinstance(res, IResource):
                res.close()

    def toSDialect(self, writer):
        writer.append("with ")
        self.resource.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        writer.append("with (")
        self.resource.toDialect(writer)
        writer.append(")")
        oneLine = len(self.instructions)==1 and isinstance(self.instructions[0], SimpleStatement)
        if not oneLine:
            writer.append(" {")
        writer.newLine()
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        if not oneLine:
            writer.append("}")
            writer.newLine()

    def toEDialect(self, writer):
        writer.append("with ")
        self.resource.toDialect(writer)
        writer.append(", do:\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
