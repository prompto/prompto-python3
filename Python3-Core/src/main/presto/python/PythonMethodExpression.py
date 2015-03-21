from __future__ import print_function
from presto.python.PythonSelectorExpression import PythonSelectorExpression
from presto.python.PythonExpressionList import PythonExpressionList
from presto.python.PythonExpression import PythonExpression
from presto.python.PythonArgument import PythonArgumentList
from presto.expression.IExpression import IExpression
from presto.value.IValue import IValue
from presto.error.NullReferenceError import NullReferenceError
import sys

#rewrite print builtin functions to allow dynamic invocation
def presto_print(objects,sep=' ', end='\n', file=None):
    # hack to ensure sys.stdout is evaluated at runtime rather than compile time
    if file is None:
        file = sys.stdout
    globals()["__builtins__"]["print"](objects,sep=sep,end=end,file=file)

#register rewritten builtin functions
rewritten = dict()
rewritten["print"] = presto_print


class PythonMethodExpression(PythonSelectorExpression):

    def __init__(self, name, args=None):
        super(PythonMethodExpression, self).__init__()
        self.name = name
        self.arguments = args if args is not None else PythonArgumentList()

    def setArguments(self, arguments):
        self.arguments = arguments

    def __str__(self):
        prefix = "" if self.parent is None else str(self.parent) + "."
        return prefix + self.name + "(" + str(self.arguments) + ")"

    def toDialect(self, writer):
        if self.parent is not None:
            self.parent.toDialect(writer)
            writer.append(".")
        writer.append(self.name)
        writer.append("(")
        self.arguments.toDialect(writer)
        writer.append(")")

    def interpret(self, context, module):
        args = self.arguments.computeArguments(context, module)
        if self.parent is None:
            return self.interpretGlobal(context, module, args)
        else:
            return self.interpretMember(context, module, args)

    def interpretGlobal(self, context, module, args):
        m = rewritten.get(self.name, None)
        if m is None:
            m = globals().get(self.name, None)
        if m is None:
            m = globals()["__builtins__"].get(self.name, None)
        if isinstance(args, tuple):
            return m(*args)
        elif isinstance(args, dict):
            return m(**args)
        else:
            return m()

    def interpretMember(self, context, module, args):
        p = self.parent.interpret(context, module)
        if p is None:
            raise NullReferenceError()
        m = getattr(p, self.name)
        if isinstance(args, tuple):
            return m(*args)
        elif isinstance(args, dict):
            return m(**args)
        else:
            return m()

