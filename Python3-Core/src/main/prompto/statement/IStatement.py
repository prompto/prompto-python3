from prompto.expression.IExpression import IExpression
from prompto.parser.ISection import ISection


class IStatement ( IExpression, ISection ):
    
    def canReturn(self):
        return False

