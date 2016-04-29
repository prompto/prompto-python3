from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.SelectorExpression import SelectorExpression
from prompto.value.NullValue import NullValue


class ItemSelector(SelectorExpression):

    def __init__(self, item, parent=None):
        super(ItemSelector, self).__init__(parent)
        self.item = item

    def getItem(self):
        return self.item

    def __str__(self):
        return str(self.parent) + "[" + str(self.item) + "]"

    def toDialect(self, writer):
        self.parent.toDialect(writer)
        writer.append("[")
        self.item.toDialect(writer)
        writer.append("]")

    def check(self, context):
        parentType = self.parent.check(context)
        itemType = self.item.check(context)
        return parentType.checkItem(context, itemType)

    def interpret(self, context):
        o = self.parent.interpret(context)
        i = self.item.interpret(context)
        if o is None or o is NullValue.instance or \
                i is None or i is NullValue.instance:
            raise NullReferenceError()
        return o.getItem(context, i)
