from prompto.expression.IExpression import IExpression
from prompto.runtime.Context import Context
from prompto.type.IType import IType
from prompto.type.TypeType import TypeType
from prompto.value.TypeValue import TypeValue


class TypeExpression(IExpression):

    def __init__(self, itype:IType):
        self.itype = itype


    def __str__(self):
        return str(self.itype)


    def check(self, context:Context):
        return TypeType(self.itype)


    def interpret(self, context:Context):
        return TypeValue(self.itype)


    def getMemberValue(self, context, name):
        return self.itype.getStaticMemberValue(context, name)


    def toDialect(self, writer):
        writer.append(str(self.itype))