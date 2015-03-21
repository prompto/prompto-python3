from presto.csharp.CSharpExpression import CSharpExpression


class CSharpParenthesisExpression ( CSharpExpression ):

    def __init__(self, expression):
        super().__init__()
        self.expression = expression;
