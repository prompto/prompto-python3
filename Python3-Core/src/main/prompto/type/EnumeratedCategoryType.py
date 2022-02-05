from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
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


    def asMutable(self, context, mutable):
        if mutable:
            pass # TODO throw
        return self


    def checkExists(self, context):
        pass # TODO


    def checkMember(self, context, name):
        if "name" == name:
            return TextType.instance
        else:
            return super(EnumeratedCategoryType, self).checkMember(context, name)


    def checkStaticMember(self, context, name):
        if "symbols" == name:
            return ListType(self)
        else:
            return super(EnumeratedCategoryType, self).checkMember(context, name)


    def getStaticMemberValue(self, context:Context, name:str):
        from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
        decl = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if not isinstance (decl, EnumeratedCategoryDeclaration):
            raise SyntaxError(self.typeName + " is not an enumerated type!")
        if "symbols" == name:
            return decl.getSymbols()
        else:
            raise SyntaxError("Unknown member:" + name)


    def getStaticMemberMethods(self, context, name):
        if name == "symbolOf":
            return [SymbolOfMethodDeclaration(self)]
        else:
            return []


class SymbolOfMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self, enumType):
        from prompto.param.CategoryParameter import CategoryParameter
        NAME_ARGUMENT = CategoryParameter(TextType.instance, "name")
        super(SymbolOfMethodDeclaration, self).__init__("symbolOf", NAME_ARGUMENT)
        self.enumType = enumType


    def interpret(self, context):
        from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
        decl = context.getRegisteredDeclaration(IDeclaration, self.enumType.typeName)
        if not isinstance(decl, EnumeratedCategoryDeclaration):
            raise SyntaxError(self.enumType.typeName + " is not an enumerated type!")
        symbolName = context.getValue("name").value
        return decl.getSymbol(symbolName)


    def check(self, context):
        return self.enumType
