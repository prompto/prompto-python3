from prompto.python.PythonExpression import PythonExpression
from prompto.runtime.Context import InstanceContext
from prompto.error.SyntaxError import SyntaxError

class PythonSelfExpression(PythonExpression):

    def __str__(self):
        return str("self")

    def toDialect(self, writer):
        writer.append("self")

    def interpret(self, context, module):
        if context is not None and not isinstance(context, InstanceContext):
            context = context.getParentContext()
        if isinstance(context, InstanceContext):
             return context.instance
        else:
            raise SyntaxError("Not in an instance context!")
