from prompto.error.InternalError import InternalError
from prompto.error.InvalidResourceError import InvalidResourceError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.runtime.Context import ResourceContext
from prompto.runtime.Variable import Variable
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.ResourceType import ResourceType
from prompto.type.TextType import TextType
from prompto.type.VoidType import VoidType
from prompto.value.IResource import IResource
from prompto.error.SyntaxError import SyntaxError
from prompto.value.TextValue import TextValue


class WriteStatement ( BaseStatement ):

    def __init__(self, content, resource, thenWith):
        super(WriteStatement, self).__init__()
        self.content = content
        self.resource = resource
        self.thenWith = thenWith


    def isSimple(self):
        return self.thenWith is None


    def __str__(self):
        return "write " + self.content.toString() + " to " + self.resource.toString()


    def check(self, context):
        resContext = context if isinstance(context, ResourceContext) else context.newResourceContext()
        resourceType = self.resource.check(resContext)
        if not isinstance(resourceType, ResourceType):
            raise SyntaxError("Not a resource!")
        if self.thenWith is None:
            return VoidType.instance
        else:
            if isinstance(context, ResourceContext):
                raise SyntaxError("Then with is only supported in simple read !")
            return self.thenWith.check(resContext, TextType.instance)


    def interpret(self, context):
        resContext = context if isinstance(context, ResourceContext) else context.newResourceContext()
        o = self.resource.interpret(resContext)
        if o is None:
            raise NullReferenceError()
        if not isinstance(o, IResource):
            raise InternalError("Illegal write source: " + o)
        if not o.isWritable():
            raise InvalidResourceError("Not writable")
        text = self.content.interpret(resContext)
        try:
            if context is resContext:
                o.writeLine(text)
            elif self.thenWith is not None:
                def callback(text):
                    local = context.newChildContext()
                    local.registerValue(Variable(self.thenWith.name, TextType.instance))
                    local.setValue(self.thenWith.name, TextValue(text))
                    self.thenWith.statements.interpret(local)
                o.writeFully(text, callback)
            else:
                o.writeFully(text)
            return None
        finally:
            if context is not resContext:
                o.close()


    def toDialect(self, writer):
        super().toDialect(writer)
        if self.thenWith is not None:
            self.thenWith.toDialect(writer, TextType.instance)


    def toMDialect(self, writer):
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
