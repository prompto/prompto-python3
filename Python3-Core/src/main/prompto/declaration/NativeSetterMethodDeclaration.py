from prompto.declaration.SetterMethodDeclaration import SetterMethodDeclaration
from prompto.type.IType import IType


class NativeSetterMethodDeclaration(SetterMethodDeclaration):

    def __init__(self, name, statements):
        super().__init__(name, statements)


    def checkStatements(self, context, returnType: IType):
        return self.statements.checkNative(context, returnType)
