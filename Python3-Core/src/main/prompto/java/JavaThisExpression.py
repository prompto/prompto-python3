from prompto.java.JavaExpression import JavaExpression

class JavaThisExpression ( JavaExpression ):

    def __init__(self):
        super().__init__("self")

    def __str__(self):
        return "this"

    def toDialect(self, writer):
        writer.append("this")