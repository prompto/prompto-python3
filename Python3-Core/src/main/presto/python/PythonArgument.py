from presto.python.PythonExpression import PythonExpression
from presto.expression.IExpression import IExpression
from presto.value.IValue import IValue

class PythonArgumentList(list):

     def __init__(self):
         super(PythonArgumentList, self).__init__()

     def computeArguments(self, context, module):
         return None

     def computeArgument(self, arg, context, module):
        if isinstance(arg, PythonExpression):
            arg = arg.interpret(context, module)
        if isinstance(arg, IExpression):
            arg = arg.interpret(context)
        if isinstance(arg, IValue):
            arg = arg.convertToPython()
        return arg

     def toDialect(self, writer):
        for arg in self:
            arg.toDialect(writer)
            writer.append(", ")
        if len(self)>0:
            writer.trimLast(2)


class PythonOrdinalArgumentList(PythonArgumentList):

    def __init__(self, expression):
        super(PythonOrdinalArgumentList, self).__init__()
        self.append(expression)

    def computeArguments(self, context, module):
        values = ()
        for arg in self:
            arg = self.computeArgument(arg, context, module)
            values = values + ( arg, )
        return values

class PythonNamedArgument(object):

    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def toDialect(self, writer):
        if self.name is not None:
            writer.append(self.name)
            writer.append("=")
        self.expression.toDialect(writer)

class PythonNamedArgumentList(PythonArgumentList):

    def __init__(self, argument=None):
        super(PythonNamedArgumentList, self).__init__()
        if argument is not None:
            self.append(argument)

    def computeArguments(self, context, module):
        values = dict()
        for named in self:
            arg = self.computeArgument(named.expression, context, module)
            values[named.name] = arg
        return values
