from prompto.param.AttributeParameter import AttributeParameter
from prompto.param.INamedParameter import INamedParameter
from prompto.param.MethodParameter import MethodParameter
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.error.SyntaxError import SyntaxError
from prompto.runtime.Context import MethodDeclarationMap


class UnresolvedParameter (INamedParameter):

    def __init__(self, name):
        super(UnresolvedParameter, self).__init__()
        self.name = name
        self.defaultValue = None
        self.resolved = None
        self.mutable = False


    def getSignature(self, dialect):
        return self.getName()


    def getName(self):
        return self.name


    def __str__(self):
        return self.name


    def setMutable(self, mutable):
        self.mutable = mutable


    def toDialect(self, writer):
        writer.append(self.name)
        if self.defaultValue is not None:
            writer.append(" = ")
            self.defaultValue.toDialect(writer)


    def check(self, context):
        self.resolveAndCheck(context)


    def getProto(self):
        return self.name


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
            self.resolved = AttributeParameter(self.name)
        elif isinstance(named, MethodDeclarationMap):
            self.resolved = MethodParameter(self.name)
        if self.resolved is not None:
            self.resolved.setMutable(self.mutable)
        else:
            raise SyntaxError("Unknown identifier:" + self.name)
