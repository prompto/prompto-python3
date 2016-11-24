from prompto.value.BaseValue import BaseValue
from prompto.value.IIterable import IIterable
from prompto.store.InvalidValueError import InvalidValueError
from prompto.runtime.Variable import Variable

class IterableValue(BaseValue, IIterable):

    def __init__(self, itemType, context, length, name, source, expression):
        from prompto.type.IteratorType import IteratorType
        super().__init__(IteratorType(itemType))
        self.itemType = itemType
        self.context = context
        self.length = length
        self.name = name
        self.source = source
        self.expression = expression

    def getIterator(self, context):
        for value in self.source:
            child = context.newChildContext()
            child.registerValue(Variable(self.name, self.itemType))
            child.setValue(self.name, value)
            value = self.expression.interpret(child)
            yield value

    def getMemberValue(self, context, name, autoCreate):
        if "count"==name:
            return self.length
        else:
            raise InvalidValueError("No such member:" + name)

