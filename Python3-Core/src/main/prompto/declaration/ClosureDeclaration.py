from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration


class ClosureDeclaration(AbstractMethodDeclaration):

    def __init__(self, closure):
        super().__init__(closure.itype.method.getName(), closure.itype.method.getArguments(), closure.itype.method.getReturnType())
        self.closure = closure

    def interpret(self, context):
        return self.closure.interpret(context)
