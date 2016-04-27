from __future__ import print_function
from prompto.python.PythonSelectorExpression import PythonSelectorExpression
from prompto.python.PythonArgument import PythonArgumentList
from prompto.error.SyntaxError import SyntaxError
from prompto.error.NullReferenceError import NullReferenceError
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
        m = self.findMethod(context, module)
        if m is None:
            raise SyntaxError("Unknown native method:" + str(self))
        args = self.arguments.computeArguments(context, module)
        if isinstance(args, tuple):
            return m(*args)
        elif isinstance(args, dict):
            return m(**args)
        else:
            return m()

    def findMethod(self, context, module):
        if self.parent is None:
            return self.findGlobal(context, module)
        else:
            return self.findMember(context, module)

    def findGlobal(self, context, module):
        m = self.findInModule(context, module)
        if m is None:
            m = rewritten.get(self.name, None)
        if m is None:
            m = globals().get(self.name, None)
        if m is None:
            m = globals()["__builtins__"].get(self.name, None)
        return m

    def findInModule(self, context, module):
        if module is None:
            return None
        else:
            try:
                m = module.resolve()
                return m.__dict__.get(self.name, None)
            except:
                return None

    def findMember(self, context, module):
        p = self.parent.interpret(context, module)
        if p is None:
            raise NullReferenceError()
        return getattr(p, self.name)

