from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.parser.Section import Section
from prompto.runtime.Context import Context
from prompto.type.IType import IType
from prompto.type.TypeType import TypeType
from prompto.utils.CodeWriter import CodeWriter
from prompto.value.TypeValue import TypeValue


class TypeLiteral(Section, IExpression):

    def __init__(self, typ:IType):
        self.typ = typ


    def check(self, context:Context):
        return TypeType(self.typ)


    def interpret(self, context:Context):
        return TypeValue(self.typ)


    def toDialect(self, writer:CodeWriter):
        if writer.dialect is Dialect.E:
            writer.append("Type: ")
        self.typ.toDialect(writer)

    def parentToDialect(self, writer:CodeWriter):
        self.typ.toDialect(writer)


    def __str__(self):
        return str(self.typ)
