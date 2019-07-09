from prompto.expression.IExpression import IExpression
from prompto.runtime.Context import Context
from prompto.type.IType import IType
from prompto.value.TypeValue import TypeValue


class TypeExpression(IExpression):

    def __init__(self, typ:IType):
        self.typ = typ


    def __str__(self):
        return str(self.typ)


    def check(self, context:Context):
        return self.typ


    def interpret(self, context:Context):
        return TypeValue(self.typ)


    def getMemberValue(self, context, name):
        return self.typ.getMemberValue(context, name)


    def toDialect(self, writer):
        writer.append(str(self.typ))