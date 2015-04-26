from presto.javascript.JavaScriptExpression import JavaScriptExpression
from presto.expression.ThisExpression import ThisExpression

class JavaScriptThisExpression ( JavaScriptExpression ):

    def __init__(self):
        super().__init__("self")
        self.expression = ThisExpression()

    def __str__(self):
        return str(self.expression)

    def toDialect(self, writer):
        self.expression.toDialect(writer)