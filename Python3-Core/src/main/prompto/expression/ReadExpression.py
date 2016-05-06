from prompto.error.InternalError import InternalError
from prompto.error.InvalidResourceError import InvalidResourceError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.IExpression import IExpression
from prompto.runtime.Context import ResourceContext
from prompto.type.ResourceType import ResourceType
from prompto.type.TextType import TextType
from prompto.value.IResource import IResource
from prompto.error.SyntaxError import SyntaxError

class ReadExpression ( IExpression ) :

    def __init__(self, resource):
        super(ReadExpression, self).__init__()
        self.resource = resource

    def __str__(self):
        return "read from " + str(self.resource)

    def check(self, context):
        context = context if isinstance(context, ResourceContext) else context.newResourceContext()
        sourceType = self.resource.check(context)
        if not isinstance(sourceType, ResourceType):
            raise SyntaxError("Not a readable resource!")
        return TextType.instance

    def interpret(self, context):
        resContext = context if isinstance(context, ResourceContext) else context.newResourceContext()
        o = self.resource.interpret(resContext)
        if o is None:
            raise NullReferenceError()
        if not isinstance(o, IResource):
            raise InternalError("Illegal read source: " + o)
        if not o.isReadable():
            raise InvalidResourceError("Not readable")
        try:
            return o.readFully()
        finally:
            if context is not resContext:
                o.close()

    def toDialect(self, writer):
        writer.append("read from ")
        self.resource.toDialect(writer)
