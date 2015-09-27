from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.IEnumeratedDeclaration import IEnumeratedDeclaration
from prompto.type.EnumeratedCategoryType import EnumeratedCategoryType

class EnumeratedCategoryDeclaration ( ConcreteCategoryDeclaration, IEnumeratedDeclaration):

    def __init__(self, name):
        super(EnumeratedCategoryDeclaration, self).__init__(name)
        self.symbols = None

    def getSymbols(self):
        return self.symbols

    def setSymbols(self, symbols):
        self.symbols = symbols
        type = EnumeratedCategoryType(self.name)
        for s in symbols:
            s.setType(type)

    def register(self, context):
        context.registerDeclaration(self)
        for symbol in self.symbols:
            context.registerValue(symbol)

    def check(self, context):
        super(EnumeratedCategoryDeclaration, self).check(context)
        for s in self.symbols:
            s.check(context) # TODO
        return self.getType(context)

    def getType(self, context):
        return EnumeratedCategoryType(self.name)

    def toODialect(self, writer):
        writer.append("enumerated category ")
        writer.append(self.name)
        if self.attributes is not None:
            writer.append('(')
            self.attributes.toDialect(writer, True)
            writer.append(")")
        if self.derivedFrom is not None:
            writer.append(" extends ")
            self.derivedFrom.toDialect(writer, True)
        writer.append(" {\n")
        writer.indent()
        for symbol in self.symbols:
            symbol.toDialect(writer)
            writer.append(";\n")
        writer.dedent()
        writer.append("}\n")

    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as enumerated ")
        if self.derivedFrom is not None:
            self.derivedFrom.toDialect(writer, True)
        else:
            writer.append("category")
        if self.attributes is not None and len(self.attributes)>0:
            if len(self.attributes)==1:
                writer.append(" with attribute ")
            else:
                writer.append(" with attributes ")
            self.attributes.toDialect(writer, True)
            if len(self.symbols)>0:
                writer.append(", and symbols:\n")
        else:
            writer.append(" with symbols:\n")
        writer.indent()
        for symbol in self.symbols:
            symbol.toDialect(writer)
            writer.append("\n")
        writer.dedent()

    def toSDialect(self, writer):
        writer.append("enum ")
        writer.append(self.name)
        writer.append("(")
        if self.derivedFrom is not None:
            self.derivedFrom.toDialect(writer, False)
            if self.attributes is not None and len(self.attributes)>0:
                writer.append(", ")
        if self.attributes is not None and len(self.attributes)>0:
            self.attributes.toDialect(writer, False)
        writer.append("):\n")
        writer.indent()
        for symbol in self.symbols:
            symbol.toDialect(writer)
            writer.append("\n")
        writer.dedent()
