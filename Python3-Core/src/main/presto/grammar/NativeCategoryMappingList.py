from presto.grammar.IDialectElement import IDialectElement
from presto.utils.ObjectList import ObjectList


class NativeCategoryMappingList ( ObjectList, IDialectElement ):

    def __init__(self, mapping = None):
        super(NativeCategoryMappingList, self).__init__()
        if mapping is not None:
            self.append(mapping)

    def toPDialect(self, writer):
        writer.append("mappings:\n")
        writer.indent()
        for m in self:
            m.toDialect(writer)
            writer.newLine()
        writer.dedent()

    def toODialect(self, writer):
        writer.append("category mappings {\n")
        writer.indent()
        for m in self:
            m.toDialect(writer)
            writer.append(';')
            writer.newLine()
        writer.dedent()
        writer.append("}")

    def toEDialect(self, writer):
        writer.append("define category mappings as:\n")
        writer.indent()
        for m in self:
            m.toDialect(writer)
            writer.newLine()
        writer.dedent()

