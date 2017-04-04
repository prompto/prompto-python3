from prompto.csharp.CSharpExpression import CSharpExpression

class CSharpThisExpression ( CSharpExpression ):

    def __init__(self):
        super().__init__("self")

    def __str__(self):
        return "this"

    def toDialect(self, writer):
        writer.append("this")