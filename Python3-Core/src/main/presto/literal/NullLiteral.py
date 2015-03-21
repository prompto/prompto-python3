from presto.expression.IExpression import IExpression
from presto.parser.Dialect import Dialect
from presto.type.NullType import NullType
from presto.value.NullValue import NullValue


class NullLiteral (IExpression):

    instance = None

    def check (self, context):
        return NullType.instance

    def interpret (self, context):
        return NullValue.instance

    def toDialect (self, writer):
        if writer.dialect is Dialect.E:
            writer.append ("nothing")
        elif writer.dialect is Dialect.O:
            writer.append ("null")
        elif writer.dialect is Dialect.P:
            writer.append ("None")

NullLiteral.instance = NullLiteral()