from presto.grammar.NativeCategoryMapping import NativeCategoryMapping


class JavaNativeCategoryMapping ( NativeCategoryMapping ):

    def __init__(self, expression):
        super(JavaNativeCategoryMapping, self).__init__()
        self.expression = expression

    def getExpression(self):
        return self.expression

    def toDialect(self, writer):
        writer.append("Java: ")
        self.expression.toDialect(writer)
