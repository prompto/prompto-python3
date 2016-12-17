from prompto.declaration.IDeclaration import IDeclaration
from prompto.store.TypeFamily import TypeFamily
from prompto.type.CategoryType import CategoryType
from prompto.type.ListType import ListType
from prompto.type.TextType import TextType
from prompto.runtime.Context import Context

from prompto.error.SyntaxError import SyntaxError

class EnumeratedCategoryType ( CategoryType ):

    def __init__(self, name):
        super(EnumeratedCategoryType, self).__init__(name, TypeFamily.ENUMERATED)

    def checkMember(self, context, name):
        if "symbols"==name:
            return ListType(self)
        elif "name"==name:
            return TextType.instance
        else:
            return super(EnumeratedCategoryType, self).checkMember(context, name)


    def getMemberValue(self, context:Context, name:str):
        from prompto.declaration.IEnumeratedDeclaration import IEnumeratedDeclaration
        decl = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if not isinstance (decl, IEnumeratedDeclaration):
            raise SyntaxError(self.typeName + " is not an enumerated type!")
        if "symbols"==name:
            return decl.getSymbols()
        else:
            raise SyntaxError("Unknown member:" + name)
