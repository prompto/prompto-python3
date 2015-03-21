from presto.declaration.IDeclaration import IDeclaration
from presto.declaration.IEnumeratedDeclaration import IEnumeratedDeclaration
from presto.runtime.Context import Context
from presto.type.BaseType import BaseType
from presto.type.ListType import ListType
from presto.type.TextType import TextType


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

