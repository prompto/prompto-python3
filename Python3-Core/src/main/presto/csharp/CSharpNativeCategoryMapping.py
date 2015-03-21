from presto.grammar.NativeCategoryMapping import NativeCategoryMapping


class CSharpNativeCategoryMapping ( NativeCategoryMapping ):

    def __init__(self, expression):
        super().__init__()
        self.expression = expression

    def toDialect(self, writer):
        writer.append("C#: ")
        self.expression.toDialect(writer)
