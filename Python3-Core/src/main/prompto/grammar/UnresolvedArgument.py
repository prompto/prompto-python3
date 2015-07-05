from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.grammar.AttributeArgument import AttributeArgument
from prompto.grammar.INamedArgument import INamedArgument
from prompto.grammar.MethodArgument import MethodArgument
from prompto.runtime.Context import MethodDeclarationMap
from prompto.error.SyntaxError import SyntaxError

class UnresolvedArgument ( INamedArgument ):

    def __init__(self, name):
        super(UnresolvedArgument, self).__init__()
        self.name = name
        self.defaultValue = None
        self.resolved = None

    def getSignature(self, dialect):
        return self.getName()

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def toDialect(self, writer):
        writer.append(self.name)
        if self.defaultValue is not None:
            writer.append(" = ")
            self.defaultValue.toDialect(writer)

    def check(self, context):
        self.resolveAndCheck(context)

    def getProto(self, context):
        self.resolveAndCheck(context)
        return self.resolved.getProto(context)

    def getType(self, context):
        self.resolveAndCheck(context)
        return self.resolved.getType(context)

    def register(self, context):
        self.resolveAndCheck(context)
        self.resolved.register(context)

    def checkValue(self, context, value):
        self.resolveAndCheck(context)
        return self.resolved.checkValue(context, value)

    def resolveAndCheck(self, context):
        if self.resolved is not None:
            return
        named = context.getRegisteredDeclaration(IDeclaration, self.name)
        if isinstance(named, AttributeDeclaration):
            self.resolved = AttributeArgument(self.name)
        elif isinstance(named, MethodDeclarationMap):
            self.resolved = MethodArgument(self.name)
        else:
            raise SyntaxError("Unknown identifier:" + self.name)
