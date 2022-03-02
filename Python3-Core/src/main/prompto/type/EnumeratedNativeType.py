from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.runtime.Context import Context
from prompto.type.BaseType import BaseType
from prompto.type.ListType import ListType
from prompto.type.TextType import TextType
from prompto.store.TypeFamily import TypeFamily
from prompto.error.SyntaxError import SyntaxError


class EnumeratedNativeType ( BaseType ):

    def __init__(self, typeName, derivedFrom):
        super(EnumeratedNativeType, self).__init__(TypeFamily.ENUMERATED)
        self.typeName = typeName
        self.derivedFrom = derivedFrom


    def getDerivedFrom(self):
        return self.derivedFrom


    def checkExists(self, context):
        pass # TODO


    def checkMember(self, context, name):
        if "name"==name:
            return TextType.instance
        elif name=="value":
            return self.derivedFrom
        else:
            return super(EnumeratedNativeType, self).checkMember(context, name)


    def checkStaticMember(self, context, name):
        if name=="symbols":
            return ListType(self)
        else:
            return super(EnumeratedNativeType, self).checkMember(context, name)


    def getStaticMemberValue(self, context:Context, name:str):
        from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
        decl = context.getRegisteredDeclaration(IDeclaration, self.typeName)
        if not isinstance (decl, EnumeratedNativeDeclaration):
            raise SyntaxError(self.typeName + " is not an enumerated type!")
        if "symbols" == name:
            return decl.getSymbols()
        else:
            raise SyntaxError("Unknown member:" + name)


    def getStaticMemberMethods(self, context, name):
        if name == "symbolOf":
            return [SymbolOfMethodDeclaration(self)]
        else:
            return super(EnumeratedNativeType, self).getStaticMemberMethods(context, name)


    def isMoreSpecificThan(self, context, itype):
        return False

class SymbolOfMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self, enumType):
        from prompto.param.CategoryParameter import CategoryParameter
        NAME_ARGUMENT = CategoryParameter(TextType.instance, "name")
        super(SymbolOfMethodDeclaration, self).__init__("symbolOf", NAME_ARGUMENT)
        self.enumType = enumType


    def interpret(self, context):
        from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
        decl = context.getRegisteredDeclaration(IDeclaration, self.enumType.typeName)
        if not isinstance(decl, EnumeratedNativeDeclaration):
            raise SyntaxError(self.enumType.typeName + " is not an enumerated type!")
        symbolName = context.getValue("name").value
        return decl.getSymbol(symbolName)


    def check(self, context):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance
