from prompto.javascript.JavaScriptExpression import JavaScriptExpression

class JavaScriptNewExpression ( JavaScriptExpression ):

    def __init__(self, method):
        super(JavaScriptNewExpression, self).__init__("")
        self.method = method

    def __str__(self):
        return "new " + str(self.method)

    def toDialect(self, writer):
        writer.append("new ")
        self.method.toDialect(writer)