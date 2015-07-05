from prompto.expression.IExpression import IExpression
from prompto.literal.Literal import *
from prompto.value.TupleValue import *
from prompto.type.TupleType import *


class TupleLiteral ( Literal ):

    def __init__(self, expressions = []):
        strs = [ str(e) for e in expressions]
        super().__init__("(" + ", ".join(strs) + ")", TupleValue())
        self.expressions = expressions

    def check(self, context):
        return TupleType.instance

    def interpret(self, context):
        if self.value.isEmpty() and len(self.expressions) >0:
            value = TupleValue()
            for o in self.expressions:
                o = o.interpret(context)
                value.items.append(o)
            self.value = value
        return self.value

    def toDialect(self, writer):
        writer.append('(')
        if len(self.expressions)>0:
            for item in self.expressions:
                item.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)
        writer.append(')')


