from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.grammar.IdentifierList import IdentifierList


class ConcreteWidgetDeclaration ( ConcreteCategoryDeclaration ):

    def __init__(self, name, derivedFrom, methods):
        super(ConcreteWidgetDeclaration, self).__init__(name, None)
        if derivedFrom is not None:
            self.setDerivedFrom(IdentifierList(derivedFrom))
        self.setMethods(methods)

    def categoryTypeToEDialect(self, writer):
        if self.derivedFrom is None:
            writer.append("widget")
        else:
            self.derivedFrom.toDialect(writer, True)

    def categoryTypeToODialect(self, writer):
        writer.append("widget")


    def categoryTypeToMDialect(self, writer):
        writer.append("widget")

