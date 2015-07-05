from prompto.javascript.JavaScriptExpression import JavaScriptExpression


class JavaScriptIdentifierExpression (JavaScriptExpression):

    @staticmethod
    def parse(ids):
        parts = ids.split("\\.")
        result = None
        for part in parts:
            result = JavaScriptIdentifierExpression(result, part)
        return result

    def __init__(self, parent, identifier):
        self.parent = parent
        self.identifier = identifier

    def __str__(self):
        if self.parent is None:
            return self.identifier
        else:
            return str(self.parent) + "." + self.identifier

    def toDialect(self, writer):
        if self.parent is not None:
            self.parent.toDialect(writer)
            writer.append('.')
        writer.append(self.identifier)
