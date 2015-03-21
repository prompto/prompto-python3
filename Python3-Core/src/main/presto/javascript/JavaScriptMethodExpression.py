from presto.javascript.JavaScriptSelectorExpression import JavaScriptSelectorExpression


class JavaScriptMethodExpression (JavaScriptSelectorExpression ):

    def __init__(self, name):
        self.name = name
        self.arguments = None

    def __str__(self):
        return (str(self.parent) + "." if self.parent is not None else "") + self.name + "(" + str(self.arguments) + ")"

    def toDialect(self, writer):
        if self.parent is not None:
            self.parent.toDialect(writer)
            writer.append('.')
        writer.append(self.name)
        writer.append('(')
        if self.arguments is not None:
            self.arguments.toDialect(writer)
        writer.append(')')
