from io import StringIO

from prompto.error.InternalError import InternalError
from prompto.literal.Literal import Literal
from prompto.type.TupleType import TupleType
from prompto.value.BaseValueList import BaseValueList
from prompto.value.IFilterable import IFilterable
from prompto.value.SetValue import SetValue
from prompto.error.SyntaxError import SyntaxError


class TupleValue ( BaseValueList, IFilterable ):

    def __init__(self, mutable, items = None, item = None):
        super().__init__(TupleType(), items)
        self.mutable = mutable
        if item is not None:
            self.items.append(item)

    def newInstance(self, items):
        return TupleValue(False, items)

    def Add(self, context, value):
        if isinstance(value, (BaseValueList, SetValue)):
            return self.merge(value)
        else:
            raise SyntaxError("Illegal: Tuple + " + type(value).__name__)

    def __str__(self):
        with StringIO() as sb:
            sb.write("(")
            for v in self.items:
                sb.write(str(v))
                sb.write(", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len - 2)
                sb.truncate(len-2)
            sb.write(")")
            return sb.getvalue()

    def toDialect(self, writer):
        writer.append('(')
        if self.size()>0:
            for o in self.items:
                if isinstance(o, Literal):
                    o.toDialect(writer)
                else:
                    writer.append(str(o))
                writer.append(", ")
            writer.trimLast(2)
        writer.append(')')

    def __hash__(self):
        return hash(frozenset(self.items))

    def filter(self, context, itemName, filter):
        result = TupleValue()
        for o in self.getIterator(context):
            context.setValue(itemName, o)
            test = filter.interpret(context)
            from prompto.value.Boolean import Boolean
            if not isinstance(test, Boolean):
                raise InternalError("Illegal test result: " + test)
            if test.getValue():
                result.append(o)
        return result
