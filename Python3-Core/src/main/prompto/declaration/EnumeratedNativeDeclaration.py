from prompto.declaration.BaseDeclaration import BaseDeclaration
from prompto.declaration.IEnumeratedDeclaration import IEnumeratedDeclaration
from prompto.type.EnumeratedNativeType import EnumeratedNativeType


class EnumeratedNativeDeclaration ( BaseDeclaration, IEnumeratedDeclaration ):

    def __init__(self, name, derivedFrom, symbols):
        super(EnumeratedNativeDeclaration, self).__init__(name)
        self.typ = EnumeratedNativeType(name, derivedFrom)
        self.symbols = symbols
        for s in symbols:
            s.setType(self.typ)


    def getSymbols(self):
        return self.symbols


    def getSymbol(self, name):
        matches = list(filter(lambda s: s.getName()==name, self.symbols))
        return matches[0] if len(matches) > 0 else None


    def __str__(self):
        return "" # TODO


    def register(self, context):
        context.registerDeclaration(self)
        for s in self.symbols:
            s.register(context)


    def check(self, context):
        for s in self.symbols:
            s.check(context)
        return self.typ


    def getType(self, context):
        return self.typ


    def toMDialect(self, writer):
        writer.append("enum ")
        writer.append(self.name)
        writer.append('(')
        self.typ.getDerivedFrom().toDialect(writer)
        writer.append("):\n")
        writer.indent()
        for symbol in self.symbols:
            symbol.toDialect(writer)
            writer.append("\n")
        writer.dedent()


    def toODialect(self, writer):
        writer.append("enumerated ")
        writer.append(self.name)
        writer.append('(')
        self.typ.getDerivedFrom().toDialect(writer)
        writer.append(") {\n")
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
        self.typ.getDerivedFrom().toDialect(writer)
        writer.append(" with symbols:\n")
        writer.indent()
        for symbol in self.symbols:
            symbol.toDialect(writer)
            writer.append("\n")
        writer.dedent()

