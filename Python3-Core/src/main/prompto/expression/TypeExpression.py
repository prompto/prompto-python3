from prompto.expression.IExpression import IExpression
from prompto.runtime.Context import Context
from prompto.type.IType import IType
from prompto.value.TypeValue import TypeValue


class TypeExpression(IExpression):

    def __init__(self, type:IType):
        self.type = type

    def __str__(self):
        return str(self.type)

    def check(self, context:Context):
        return self.type

    def interpret(self, context:Context):
        return TypeValue(self.type)

    def getMember(self, context, name):
        return self.type.getMember(context, name)

    def toDialect(self, writer):
        self.type.toDialect(writer)