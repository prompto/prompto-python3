from io import StringIO

from presto.error.InternalError import InternalError
from presto.expression.IExpression import IExpression
from presto.type.TextType import TextType
from presto.type.DictType import DictType
from presto.type.MissingType import MissingType
from presto.value.BaseValue import BaseValue
from presto.value.IContainer import IContainer
from presto.value.IValue import IValue
from presto.value.Integer import Integer
from presto.value.ListValue import ListValue


class Dictionary(BaseValue, IContainer):

    @staticmethod
    def merge(dict1, dict2):
        return Dictionary(dict1.type.itemType, value=dict(dict1.value, **dict2.value))

    def __init__(self, itemType, copyFrom=None, value=None):
        super().__init__(DictType(itemType))
        if copyFrom != None:
            self.value = copyFrom.value
        elif value != None:
            self.value = value
        else:
            self.value = dict()

    def size(self):
        return len(self.value)


    def isEmpty(self):
        return len(self.value) == 0


    def Add(self, context, value):
        if isinstance(value, Dictionary):
            return Dictionary.merge(self, value)
        else:
            raise SyntaxError("Illegal: Dict + " + type(value).__name__)


    def hasItem(self, context, value):
        from presto.value.Text import Text
        if isinstance(value, Text):
            return self.value.get(value.value, None) is not None
        else:
            raise SyntaxError("Only Text key is supported by " + type(self).__name__)


    def getMember(self, context, name):
        if "length" == name:
            return Integer(self.size())
        elif "keys" == name:
            from presto.value.Text import Text
            res = [Text(k) for k in self.value.keys()]
            return ListValue(TextType.instance, items=res)
        elif "values" == name:
            return ListValue(self.type.itemType, items=self.value.values())
        else:
            raise SyntaxError("No such member:" + name)

    def getItem(self, context, item):
        from presto.value.Text import Text
        if isinstance(item, Text):
            value = self.value.get(item.value, None)
            if isinstance(value, IValue):
                return value
            else:
                raise InternalError("Item not a value!")
        else:
            raise SyntaxError("No such item:" + str(item))


    def ConvertTo(self, type_):
        return self


    def __eq__(self, obj):
        if not isinstance(obj, Dictionary):
            return False
        return self.value == obj.value


    def __str__(self):
        with StringIO() as sb:
            sb.write("{")
            for k, v in self.value.items():
                sb.write(k)
                sb.write(":")
                sb.write(str(v))
                sb.write(", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len - 2)
                sb.truncate(len - 2)
            sb.write("}")
            return sb.getvalue()

    def getKeys(self):
        from presto.value.Text import Text
        for k in iter(self.value.keys()):
            yield Text(k)


    def getItems(self, context):
        for k, v in iter(self.value.items()):
            yield KVPValue(k, v)


class KVPValue(BaseValue):

    def __init__(self, key, value):
        super(KVPValue, self).__init__(MissingType.instance)
        from presto.value.Text import Text
        self.key = Text(key)
        self.value = value

    def getMember(self, context, name):
        if "key" == name:
            return self.key
        elif "value" == name:
            value = self.value
            if isinstance(value, IExpression):
                value = value.interpret(context)
            return value
        else:
            raise SyntaxError("No such member:" + name)
