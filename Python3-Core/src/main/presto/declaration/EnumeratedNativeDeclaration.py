from presto.declaration.BaseDeclaration import *
from presto.declaration.IEnumeratedDeclaration import *
from presto.type.EnumeratedNativeType import *


class EnumeratedNativeDeclaration ( BaseDeclaration, IEnumeratedDeclaration ):

    def __init__(self, name, derivedFrom, symbols):
        super(EnumeratedNativeDeclaration, self).__init__(name)
        self.type = EnumeratedNativeType(name, derivedFrom)
        self.symbols = symbols
        for s in symbols:
            s.setType(self.type)

    def getSymbols(self):
        return self.symbols

    def __str__(self):
        return "" # TODO

    def register(self, context):
        context.registerDeclaration(self)
        for s in self.symbols:
            s.register(context)

    def check(self, context):
        for s in self.symbols:
            s.check(context)
        return self.type

    def getType(self, context):
        return self.type

    def toPDialect(self, writer):
        writer.append("enum ")
        writer.append(self.name)
        writer.append('(')
        self.type.getDerivedFrom().toDialect(writer)
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
        self.type.getDerivedFrom().toDialect(writer)
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
        writer.append(" as: enumerated ")
        self.type.getDerivedFrom().toDialect(writer)
        writer.append(" with symbols:\n")
        writer.indent()
        for symbol in self.symbols:
            symbol.toDialect(writer)
            writer.append("\n")
        writer.dedent()

