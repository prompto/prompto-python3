from prompto.expression.IExpression import IExpression
from prompto.literal.Literal import *
from prompto.value.TupleValue import *
from prompto.type.TupleType import *


class TupleLiteral ( Literal ):

    def __init__(self, mutable, expressions = []):
        strs = [ str(e) for e in expressions]
        super().__init__("(" + ", ".join(strs) + ")", TupleValue(False))
        self.mutable = mutable
        self.expressions = expressions

    def check(self, context):
        return TupleType.instance

    def interpret(self, context):
        if len(self.expressions) >0:
            value = TupleValue(self.mutable)
            for o in self.expressions:
                o = o.interpret(context)
                value.items.append(o)
            return value
        else:
            return self.value

    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        writer.append('(')
        if len(self.expressions)>0:
            for item in self.expressions:
                item.toDialect(writer)
                writer.append(", ")
            if len(self.expressions)==1:
                writer.trimLast(1)
            else:
                writer.trimLast(2)
        writer.append(')')


