from presto.javascript.JavaScriptExpression import JavaScriptExpression

class JavaScriptLiteral (JavaScriptExpression):

    def __init__(self, text):
        super(JavaScriptLiteral,self).__init__()
        self.text = text

    def toDialect(self, writer):
        writer.append(self.text)

