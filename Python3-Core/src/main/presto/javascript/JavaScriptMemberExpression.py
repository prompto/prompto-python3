from presto.javascript.JavaScriptSelectorExpression import JavaScriptSelectorExpression


class JavaScriptMemberExpression (JavaScriptSelectorExpression ):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return (str(self.parent) + "." if self.parent is not None else "") + self.name

    def toDialect(self, writer):
        if self.parent is not None:
            self.parent.toDialect(writer)
            writer.append('.')
        writer.append(self.name)
