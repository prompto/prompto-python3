from prompto.error.InternalError import InternalError
from prompto.error.InvalidResourceError import InvalidResourceError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.IExpression import IExpression
from prompto.runtime.Context import ResourceContext
from prompto.type.ResourceType import ResourceType
from prompto.type.TextType import TextType
from prompto.value.IResource import IResource
from prompto.error.SyntaxError import SyntaxError

class ReadOneExpression ( IExpression ) :

    def __init__(self, resource):
        super().__init__()
        self.resource = resource



    def __str__(self):
        return "read one from " + str(self.resource)



    def check(self, context):
        if not isinstance(context, ResourceContext):
            raise SyntaxError("Not a resource context!")
        sourceType = self.resource.check(context)
        if not isinstance(sourceType, ResourceType):
            raise SyntaxError("Not a readable resource!")
        return TextType.instance



    def interpret(self, context):
        if not isinstance(context, ResourceContext):
            raise SyntaxError("Not a resource context!")
        o = self.resource.interpret(context)
        if o is None:
            raise NullReferenceError()
        if not isinstance(o, IResource):
            raise InternalError("Illegal read source: " + o)
        if not o.isReadable():
            raise InvalidResourceError("Not readable")
        return o.readLine()



    def toDialect(self, writer):
        writer.append("read one from ")
        self.resource.toDialect(writer)
