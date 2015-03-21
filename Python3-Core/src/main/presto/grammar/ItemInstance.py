from presto.error.IndexOutOfRangeError import IndexOutOfRangeError
from presto.error.InvalidDataError import InvalidDataError
from presto.grammar.IAssignableInstance import IAssignableInstance
from presto.type.IntegerType import IntegerType
from presto.value.IContainer import IContainer
from presto.value.IValue import IValue
from presto.value.Integer import Integer
from presto.value.ListValue import ListValue


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

    def toDialect(self, writer):
        self.parent.toDialect(writer)
        writer.append('[')
        self.item.toDialect(writer)
        writer.append(']')

    def checkAssignValue(self, context, expression):
        self.parent.checkAssignElement(context)
        itemType = self.item.check(context)
        if itemType!=IntegerType.instance:
            raise SyntaxError("Expecting an Integer, got:" + str(itemType))

    def checkAssignMember(self, context, memberName):
        pass

    def checkAssignElement(self, context):
        pass

    def assign(self, context, expression):
        obj = self.parent.interpret(context)
        if not isinstance(obj, ListValue):
            raise InvalidDataError("Expected a List, got:" + type(obj).getName())
        idx = self.item.interpret(context)
        if not isinstance(idx, Integer):
            raise InvalidDataError("Expected an Integer, got:" + type(idx).getName())
        index = idx.IntegerValue()
        if index<1 or index>obj.size():
            raise IndexOutOfRangeError()
        obj.setItem(index-1,expression.interpret(context))

    def interpret(self, context):
        parent = self.parent.interpret(context)
        item = self.item.interpret(context)
        if isinstance(parent, IContainer) and isinstance(item, IValue):
            return parent.getItem(context, item)
        else:
            raise SyntaxError("Unknown item/key: " + type(item).getName())
