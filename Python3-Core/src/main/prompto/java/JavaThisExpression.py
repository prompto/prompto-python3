from prompto.java.JavaExpression import JavaExpression
from prompto.expression.ThisExpression import ThisExpression

class JavaThisExpression ( JavaExpression ):

    def __init__(self):
        super().__init__("self")
        self.expression = ThisExpression()

    def __str__(self):
        return str(self.expression)

    def toDialect(self, writer):
        self.expression.toDialect(writer)