from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration


class ClosureDeclaration(AbstractMethodDeclaration):

    def __init__(self, closure):
        super().__init__(closure.type.method.getName(), closure.type.method.getArguments(), closure.type.method.getReturnType())
        self.closure = closure

    def interpret(self, context):
        return self.closure.interpret(context)
