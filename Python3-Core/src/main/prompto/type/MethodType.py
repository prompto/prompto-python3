from prompto.declaration.IDeclaration import IDeclaration
from prompto.runtime.Context import MethodDeclarationMap
from prompto.type.BaseType import BaseType
from prompto.error.SyntaxError import SyntaxError

class MethodType(BaseType):
    def __init__(self, context, name):
        super(MethodType, self).__init__(name)
        self.context = context;

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj == None:
            return False
        if not isinstance(obj, MethodType):
            return False
        return self.getName() == obj.getName()

    def checkUnique(self, context):
        actual = context.getRegisteredDeclaration(IDeclaration, self.name)
        if actual != None:
            raise SyntaxError("Duplicate name: \"" + self.name + "\"")

    def getDeclaration(self, context):
        map = self.context.getRegisteredDeclaration(MethodDeclarationMap, self.name)
        if map == None:
            raise SyntaxError("Unknown method: \"" + self.name + "\"")
        return iter(map.values()).__next__()

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
