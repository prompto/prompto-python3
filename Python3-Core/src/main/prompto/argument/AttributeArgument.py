from prompto.argument.BaseArgument import BaseArgument
from prompto.argument.INamedArgument import INamedArgument
from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.IDeclaration import IDeclaration


class AttributeArgument ( BaseArgument, INamedArgument ):

    def __init__(self, name):
        super(AttributeArgument, self).__init__(name)

    def getSignature(self, dialect):
        return self.getName()

    def __str__(self):
        return self.getName()

    def getProto(self):
        return self.getName()

    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, AttributeArgument):
            return False
        return self.getName()==obj.getName()

    def register(self, context):
        context.registerValue(self, True)
        if self.defaultExpression is not None:
            context.setValue(self.name, self.defaultExpression)

    def check(self, context):
        actual = context.getRegisteredDeclaration(AttributeDeclaration,self.name)
        if actual is None:
            raise SyntaxError("Unknown attribute: \"" + self.name + "\"")

    def getType(self, context):
        named = context.getRegisteredDeclaration(IDeclaration,self.name)
        return named.getType(context)

    def checkValue(self, context, value):
        actual = context.getRegisteredDeclaration(AttributeDeclaration,self.name)
        return actual.checkValue(context,value)

