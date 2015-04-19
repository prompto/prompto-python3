from presto.grammar.NativeCategoryBinding import NativeCategoryBinding


class CSharpNativeCategoryBinding ( NativeCategoryBinding ):

    def __init__(self, expression):
        super().__init__()
        self.expression = expression

    def toDialect(self, writer):
        writer.append("C#: ")
        self.expression.toDialect(writer)
