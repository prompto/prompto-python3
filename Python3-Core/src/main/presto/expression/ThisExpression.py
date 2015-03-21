from presto.expression.IExpression import IExpression
from presto.parser.Dialect import Dialect
from presto.runtime.Context import InstanceContext
from presto.error.SyntaxError import SyntaxError

class ThisExpression(IExpression):

    def check (self, context):
        if context is not None and not isinstance(context, InstanceContext):
            context = context.getParentContext ()
        if isinstance(context, InstanceContext):
            return context.instanceType
        else:
            raise SyntaxError ("Not in an instance context!")

    def interpret (self, context):
        if context is not None and not isinstance(context, InstanceContext):
            context = context.getParentContext ()
        if isinstance(context, InstanceContext):
            return context.instance
        else:
            raise SyntaxError ("Not in an instance context!")

    def toDialect (self, writer):
        if writer.dialect == Dialect.O:
            writer.append ("this")
        else:
            writer.append ("self")
