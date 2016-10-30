
from prompto.error.NotMutableError import NotMutableError
from prompto.error.SyntaxError import SyntaxError
from prompto.instance.IAssignableInstance import IAssignableInstance
from prompto.type.AnyType import AnyType
from prompto.value.IContainer import IContainer
from prompto.value.IValue import IValue


class ItemInstance ( IAssignableInstance ):

    def __init__(self, parent, item):
        super().__init__()
        self.parent = parent
        self.item = item

    def setParent(self, parent):
        self.parent = parent

    def getItem(self):
        return self.item

    def __str__(self):
        return str(self.parent) + "[" + str(self.item) + "]"

    def toDialect(self, writer, expression):
        self.parent.toDialect(writer, None)
        writer.append('[')
        self.item.toDialect(writer)
        writer.append(']')

    def checkAssignValue(self, context, valueType):
        itemType = self.item.check(context)
        return self.parent.checkAssignItem(context, itemType, valueType)


    def checkAssignMember(self, context, name, valueType):
        return AnyType.instance


    def checkAssignItem(self, context, itemType, valueType):
        return AnyType.instance



    def assign(self, context, expression):
        root = self.parent.interpret(context)
        if not root.mutable:
            raise NotMutableError()
        item = self.item.interpret(context)
        value = expression.interpret(context)
        root.setItem(context, item, value)



    def interpret(self, context):
        parent = self.parent.interpret(context)
        item = self.item.interpret(context)
        if isinstance(parent, IContainer) and isinstance(item, IValue):
            return parent.getItem(context, item)
        else:
            raise SyntaxError("Unknown item/key: " + type(item).getName())
