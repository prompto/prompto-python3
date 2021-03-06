from io import StringIO

from prompto.value.BaseValue import BaseValue
from prompto.value.IFilterable import IFilterable
from prompto.value.IIterable import IIterable
from prompto.runtime.Variable import Variable
from prompto.value.ListValue import ListValue
from prompto.value.SetValue import SetValue


class IterableValue(BaseValue, IIterable, IFilterable):

    def __init__(self, context, name, itemType, source, length, expression):
        from prompto.type.IteratorType import IteratorType
        super().__init__(IteratorType(itemType))
        self.context = context
        self.name = name
        self.itemType = itemType
        self.source = source
        self.length = length
        self.expression = expression


    def getIterator(self, context):
        for value in self.source:
            child = context.newChildContext()
            child.registerValue(Variable(self.name, self.itemType))
            child.setValue(self.name, value)
            value = self.expression.interpret(child)
            yield value


    def getMemberValue(self, context, name, autoCreate=False):
        if "count"==name:
            return self.length
        else:
            return super().getMemberValue(context, name, autoCreate)


    def filter(self, predicate):
        items = []
        for value in self.source:
            if predicate(value):
                items.append(value)
        return ListValue(self.itemType, items)


    def __str__(self):
        with StringIO() as sb:
            for item in self.getIterator(self.context):
                sb.write(str(item))
                sb.write(", ")
            len = sb.tell()
            if len > 0:
                sb.truncate(len - 2)
            return sb.getvalue()


    def toListValue(self, context):
        items = [ item for item in self.getIterator(context)]
        return ListValue(self.itemType, items=items)


    def toSetValue(self, context):
        items = [ item for item in self.getIterator(context)]
        return SetValue(self.itemType, items=set(items))
