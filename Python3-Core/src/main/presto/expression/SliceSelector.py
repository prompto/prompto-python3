from presto.error.NullReferenceError import NullReferenceError
from presto.expression.SelectorExpression import SelectorExpression
from presto.type.IntegerType import IntegerType
from presto.value.ISliceable import ISliceable
from presto.value.Integer import Integer
from presto.error.SyntaxError import SyntaxError

class SliceSelector(SelectorExpression):

    def __init__(self, first=None, last=None, parent=None):
        super(SliceSelector, self).__init__(parent)
        self.first = first
        self.last = last


    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

    def __str__(self):
        return str(self.parent) + "[" + \
               ("" if self.first is None else str(self.first) + ":") + \
               ("" if self.last is None else str(self.last) + "]")

    def toDialect(self, writer):
        self.parent.toDialect(writer)
        writer.append('[')
        if self.first is not None:
            self.first.toDialect(writer)
        writer.append(':')
        if self.last is not None:
            self.last.toDialect(writer)
        writer.append(']')

    def check(self, context):
        firstType = None if self.first is None else self.first.check(context)
        lastType = None if self.last is None else self.last.check(context)
        if firstType is not None and not isinstance(firstType, IntegerType):
            raise SyntaxError(str(firstType) + " is not an integer")
        if lastType is not None and not isinstance(lastType, IntegerType):
            raise SyntaxError(str(lastType) + " is not an integer")
        parentType = self.parent.check(context)
        return parentType.checkSlice(context)

    def interpret(self, context):
        o = self.parent.interpret(context)
        if o is None:
            raise NullReferenceError()
        if isinstance(o, ISliceable):
            fi = None if self.first is None else self.first.interpret(context)
            if fi is not None and not isinstance(fi, Integer):
                raise SyntaxError("Illegal sliced type: " + str(fi))
            li = None if self.last is None else self.last.interpret(context)
            if li is not None and not isinstance(li, Integer):
                raise SyntaxError("Illegal sliced type: " + str(li))
            return o.slice(fi, li)
        else:
            raise SyntaxError("Illegal sliced object: " + self.parent)
