from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import InstanceContext, DocumentContext
from prompto.error.SyntaxError import SyntaxError
from prompto.type.DocumentType import DocumentType


class ThisExpression(IExpression):

    def check (self, context):
        if isinstance(context, DocumentContext):
            return DocumentType.instance
        if context is not None and not isinstance(context, InstanceContext):
            context = context.getParentContext ()
        if isinstance(context, InstanceContext):
            return context.instanceType
        else:
            raise SyntaxError ("Not in an instance context!")

    def interpret (self, context):
        if isinstance(context, DocumentContext):
            return context.document
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
