from prompto.declaration.IDeclaration import IDeclaration
from prompto.runtime.Context import MethodDeclarationMap
from prompto.type.BaseType import BaseType
from prompto.error.SyntaxError import SyntaxError
from prompto.store.TypeFamily import TypeFamily



class MethodType(BaseType):
    def __init__(self, context, typeName):
        super(MethodType, self).__init__(TypeFamily.METHOD)
        self.typeName = typeName
        self.context = context

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, MethodType):
            return False
        return self.typeName == obj.typeName

    def checkUnique(self, context):
        actual = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if actual is not None:
            raise SyntaxError("Duplicate name: \"" + self.typeName + "\"")

    def getDeclaration(self, context):
        map = self.context.getRegisteredDeclaration(MethodDeclarationMap, self.typeName)
        if map is None:
            raise SyntaxError("Unknown method: \"" + self.typeName + "\"")
        for value in map.values():
            return value


    def checkExists(self, context):
        self.getDeclaration(context)

    def isAssignableTo(self, context, other):
        if not isinstance(other, MethodType):
            return False
        try:
            selfMethod = self.getDeclaration(context)
            otherMethod = other.getDeclaration(context)
            return selfMethod.getProto(context) == otherMethod.getProto(other.context)  # TODO: refine
        except SyntaxError:
            return False

    def isMoreSpecificThan(self, context, other):
        # TODO Auto-generated method stub
        return False
