from prompto.declaration.IDeclaration import IDeclaration
from prompto.declaration.IEnumeratedDeclaration import IEnumeratedDeclaration
from prompto.runtime.Context import Context
from prompto.type.BaseType import BaseType
from prompto.type.ListType import ListType
from prompto.type.TextType import TextType


class EnumeratedNativeType ( BaseType ):

    def __init__(self, name, derivedFrom):
        super(EnumeratedNativeType, self).__init__(name)
        self.derivedFrom = derivedFrom

    def getDerivedFrom(self):
        return self.derivedFrom

    def checkMember(self, context, name):
        if name=="symbols":
            return ListType(self.derivedFrom)
        elif "name"==name:
            return TextType.instance
        elif name=="value":
            return self
        else:
            return super(EnumeratedNativeType, self).checkMember(context, name)

    def getMember(self, context:Context, name:str):
        decl = context.getRegisteredDeclaration(IDeclaration, self.name)
        if not isinstance (decl, IEnumeratedDeclaration):
            raise SyntaxError(self.name + " is not an enumerated type!");
        if "symbols"==name:
            return decl.getSymbols()
        else:
            raise SyntaxError("Unknown member:" + name)

