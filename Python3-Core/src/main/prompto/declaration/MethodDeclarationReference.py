from prompto.declaration.MethodDeclarationWrapper import MethodDeclarationWrapper


class MethodDeclarationReference(MethodDeclarationWrapper):

    def __init__(self, wrapped):
        super(MethodDeclarationReference, self).__init__(wrapped)

    def isReference(self):
        return True

