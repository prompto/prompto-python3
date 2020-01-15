from prompto.expression.IExpression import IExpression
from prompto.expression.ThisExpression import ThisExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import InstanceContext, DocumentContext
from prompto.error.SyntaxError import SyntaxError
from prompto.type.CategoryType import CategoryType
from prompto.type.DocumentType import DocumentType


class SuperExpression(ThisExpression):

    def check (self, context):
        return self.getSuperType(context)


    def getSuperType(self, context):
        if context is not None and not isinstance(context, InstanceContext):
            context = context.getParentContext ()
        if isinstance(context, InstanceContext):
            typ = context.instanceType
            if isinstance(typ, CategoryType):
                return typ.getSuperType(context)
            else:
                return typ
        else:
            raise SyntaxError ("Not in an instance context!")

    def toDialect (self, writer):
        writer.append ("super")
