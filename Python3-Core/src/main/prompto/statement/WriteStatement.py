from prompto.error.InternalError import InternalError
from prompto.error.InvalidResourceError import InvalidResourceError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.ResourceType import ResourceType
from prompto.type.VoidType import VoidType
from prompto.value.IResource import IResource
from prompto.error.SyntaxError import SyntaxError

class WriteStatement ( SimpleStatement ):

    def __init__(self, content, resource):
        super(WriteStatement, self).__init__()
        self.content = content
        self.resource = resource

    def __str__(self):
        return "write " + self.content.toString() + " to " + self.resource.toString()

    def check(self, context):
        context = context.newResourceContext()
        resourceType = self.resource.check(context)
        if not isinstance(resourceType, ResourceType):
            raise SyntaxError("Not a resource!")
        return VoidType.instance

    def interpret(self, context):
        context = context.newResourceContext()
        o = self.resource.interpret(context)
        if o is None:
            raise NullReferenceError()
        if not isinstance(o, IResource):
            raise InternalError("Illegal write source: " + o)
        if not o.isWritable():
            raise InvalidResourceError("Not writable")
        text = self.content.interpret(context)
        o.writeFully(text)
        return None

    def toSDialect(self, writer):
        writer.append("write ")
        self.content.toDialect(writer)
        writer.append(" to ")
        self.resource.toDialect(writer)

    def toODialect(self, writer):
        writer.append("write ")
        writer.append("(")
        self.content.toDialect(writer)
        writer.append(")")
        writer.append(" to ")
        self.resource.toDialect(writer)

    def toEDialect(self, writer):
        writer.append("write ")
        self.content.toDialect(writer)
        writer.append(" to ")
        self.resource.toDialect(writer)
