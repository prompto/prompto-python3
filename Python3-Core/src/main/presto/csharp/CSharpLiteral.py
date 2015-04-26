from presto.csharp.CSharpExpression import CSharpExpression

class CSharpLiteral (CSharpExpression):

    def __init__(self, text):
        super(CSharpLiteral,self).__init__(text)

    def toDialect(self, writer):
        writer.append(self.text)
