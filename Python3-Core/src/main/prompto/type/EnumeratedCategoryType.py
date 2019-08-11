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

    def checkMember(self, context, name):
        if "symbols"==name:
            return ListType(self)
        elif "name"==name:
            return TextType.instance
        else:
            return super(EnumeratedCategoryType, self).checkMember(context, name)


    def getMemberValue(self, context:Context, name:str):
        from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
        decl = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if not isinstance (decl, EnumeratedCategoryDeclaration):
            raise SyntaxError(self.typeName + " is not an enumerated type!")
        if "symbols"==name:
            return decl.getSymbols()
        else:
            raise SyntaxError("Unknown member:" + name)


    def getMemberMethods(self, context, name):
        if name == "symbolOf":
            return [SymbolOfMethodDeclaration(self)]
        else:
            return super(EnumeratedCategoryType, self).getMemberMethods(context, name)


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


    def check(self, context, isStart):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance
