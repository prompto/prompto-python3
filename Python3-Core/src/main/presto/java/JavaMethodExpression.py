from presto.java.JavaSelectorExpression import JavaSelectorExpression
from presto.java.JavaExpressionList import JavaExpressionList

class JavaMethodExpression ( JavaSelectorExpression ):

    def __init__(self, name, args):
        self.name = name
        self.arguments = args if args is not None else JavaExpressionList()

    def addArgument(self, expression):
        self.arguments.append(expression)


    def __str__(self):
        return str(self.parent) + "." + self.name + "(" + str(self.arguments) + ")";

    def toDialect(self, writer):
        if self.parent is not None:
            self.parent.toDialect(writer)
            writer.append(".")
        writer.append(self.name)
        writer.append("(")
        self.arguments.toDialect(writer)
        writer.append(")")

