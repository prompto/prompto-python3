from presto.csharp.CSharpSelectorExpression import CSharpSelectorExpression
from presto.csharp.CSharpExpressionList import CSharpExpressionList

class CSharpMethodExpression ( CSharpSelectorExpression ):

    def __init__(self, name, arguments = None):
        self.name = name
        self.arguments = arguments if arguments is not None else CSharpExpressionList()

    def addArgument(self, expression):
        self.arguments.append(expression)


    def __str__(self):
        return str(self.parent) + "." + self.name + "(" + str(self.arguments) + ")"

    def toDialect(self, writer):
        self.parent.toDialect(writer)
        writer.append(".")
        writer.append(self.name)
        writer.append("(")
        self.arguments.toDialect(writer)
        writer.append(")")
