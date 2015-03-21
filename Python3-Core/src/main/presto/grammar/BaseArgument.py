from presto.grammar.IArgument import IArgument


class BaseArgument ( IArgument ) :

    def __init__(self, name):
        self.name = name
        self.defaultExpression = None

    def getName(self):
        return self.name

    def checkValue(self, context, expression):
        return expression.interpret(context)
