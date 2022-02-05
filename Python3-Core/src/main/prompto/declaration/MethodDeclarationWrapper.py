from prompto.declaration.IMethodDeclaration import IMethodDeclaration

class MethodDeclarationWrapper(IMethodDeclaration):

    def __init__(self, wrapped):
        super(MethodDeclarationWrapper, self).__init__()
        self.wrapped = wrapped
        self.name = wrapped.name
        self.parameters = wrapped.parameters
        self.returnType = wrapped.returnType
        self.memberOf = wrapped.memberOf

    def isAssignableTo(self, context, arguments, checkInstance):
        return self.wrapped.isAssignableTo(context, arguments, checkInstance)

    def isAbstract(self):
        return self.wrapped.isAbstract()

    def registerParameters(self, result):
        self.wrapped.registerParameters(result)

    def getProto(self):
        return self.wrapped.getProto()

    def check(self, context):
        return self.wrapped.check(context)