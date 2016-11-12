from prompto.declaration.IDeclaration import IDeclaration
from prompto.runtime.Context import MethodDeclarationMap
from prompto.type.BaseType import BaseType
from prompto.error.SyntaxError import SyntaxError
from prompto.store.TypeFamily import TypeFamily



class MethodType(BaseType):

    def __init__(self, method):
        super(MethodType, self).__init__(TypeFamily.METHOD)
        self.method = method
        self.typeName = method.name

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, MethodType):
            return False
        return self.method.getProto() == obj.method.getProto()

    def checkUnique(self, context):
        actual = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if actual is not None:
            raise SyntaxError("Duplicate name: \"" + self.typeName + "\"")

    def checkExists(self, context):
        pass


    def isMoreSpecificThan(self, context, other):
        # TODO Auto-generated method stub
        return False
