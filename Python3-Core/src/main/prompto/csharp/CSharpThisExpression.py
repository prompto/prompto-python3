from prompto.csharp.CSharpExpression import CSharpExpression
from prompto.expression.ThisExpression import ThisExpression

class CSharpThisExpression ( CSharpExpression ):

    def __init__(self):
        super().__init__("self")
        self.expression = ThisExpression()

    def __str__(self):
        return str(self.expression)

    def toDialect(self, writer):
        self.expression.toDialect(writer)