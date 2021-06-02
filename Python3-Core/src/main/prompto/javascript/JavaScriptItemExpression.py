from prompto.javascript.JavaScriptSelectorExpression import JavaScriptSelectorExpression


class JavaScriptItemExpression (JavaScriptSelectorExpression ):

    def __init__(self, exp):
        super().__init__()
        self.exp = exp

    def __str__(self):
        return str(self.parent) + "[" + str(self.exp) + "]"

    def toDialect(self, writer):
        self.parent.toDialect(writer)
        writer.append('[')
        writer.append(self.exp)
        writer.append(']')
