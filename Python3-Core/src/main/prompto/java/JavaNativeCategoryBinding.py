from prompto.grammar.NativeCategoryBinding import NativeCategoryBinding


class JavaNativeCategoryBinding ( NativeCategoryBinding ):

    def __init__(self, expression):
        super(JavaNativeCategoryBinding, self).__init__()
        self.expression = expression

    def getExpression(self):
        return self.expression

    def toDialect(self, writer):
        writer.append("Java: ")
        self.expression.toDialect(writer)
