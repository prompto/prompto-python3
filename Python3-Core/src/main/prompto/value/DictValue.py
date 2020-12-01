from io import StringIO

from prompto.error.InternalError import InternalError
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.IExpression import IExpression
from prompto.type.TextType import TextType
from prompto.type.DictType import DictType
from prompto.type.MissingType import MissingType
from prompto.value.BaseValue import BaseValue
from prompto.value.IContainer import IContainer
from prompto.value.IValue import IValue
from prompto.value.IntegerValue import IntegerValue
from prompto.value.ListValue import ListValue
from prompto.value.NullValue import NullValue
from prompto.value.SetValue import SetValue
from prompto.value.TextValue import TextValue


class DictValue(BaseValue, IContainer):

    @staticmethod
    def merge(dict1, dict2):
        return DictValue(dict1.itype.itemType, False, value=dict(dict1.value, **dict2.value))

    def __init__(self, itemType, mutable=False, copyFrom=None, value=None):
        super().__init__(DictType(itemType))
        self.mutable = mutable
        if copyFrom is not None:
            self.value = copyFrom.value
        elif value is not None:
            self.value = value
        else:
            self.value = dict()

    def size(self):
        return len(self.value)


    def isEmpty(self):
        return len(self.value) == 0


    def Add(self, context, value):
        if isinstance(value, DictValue):
            return DictValue.merge(self, value)
        else:
            raise SyntaxError("Illegal: Dict + " + type(value).__name__)


    def swap(self, context):
        swapped = DictValue(TextType.instance, True)
        for k,v in self.value.items():
            if not isinstance(v, TextValue):
                v = TextValue(v.getMember(context, "text", False))
            swapped.setItem(context, v, k)
        swapped.mutable = False
        return swapped


    def removeKey(self, key):
        self.value.pop(key.value)


    def removeValue(self, value):
        keys = set()
        for k, v in self.value.items():
            if value == v:
                keys.add(k)
        for k in keys:
            self.value.pop(k)


    def hasItem(self, context, value):
        if isinstance(value, TextValue):
            return self.value.get(value.value, None) is not None
        else:
            raise SyntaxError("Only Text key is supported by " + type(self).__name__)


    def getMemberValue(self, context, name, autoCreate=False):
        if "count" == name:
            return IntegerValue(self.size())
        elif "keys" == name:
            res = set([TextValue(k) for k in self.value.keys()])
            return SetValue(TextType.instance, items=res)
        elif "values" == name:
            return ListValue(self.itype.itemType, items=self.value.values())
        else:
            return super().getMemberValue(context, name, autoCreate)


    def setItem(self, context, item, value):
        if isinstance(item, TextValue):
            self.value[item.value] = value
        else:
            raise SyntaxError("No such item:" + str(item))


    def getItem(self, context, item):
        if isinstance(item, TextValue):
            value = self.value.get(item.value, NullValue.instance)
            if isinstance(value, IValue):
                return value
            else:
                raise InternalError("Item not a value!")
        else:
            raise SyntaxError("No such item:" + str(item))


    def convertToPython(self):
        keys = [ key for key in self.value.keys()]
        values = [ self.value.get(key).convertToPython() for key in keys]
        return dict(zip ( keys, values))


    def __eq__(self, obj):
        if not isinstance(obj, DictValue):
            return False
        return self.value == obj.value


    def __str__(self):
        with StringIO() as sb:
            sb.write("<")
            for k, v in self.value.items():
                sb.write('"')
                sb.write(k)
                sb.write('":')
                sb.write(str(v))
                sb.write(", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len - 2)
                sb.truncate(len - 2)
            else:
                sb.write(":")
            sb.write(">")
            return sb.getvalue()

    def getKeys(self):
        for k in iter(self.value.keys()):
            yield TextValue(k)


    def getIterator(self, context):
        for k, v in iter(self.value.items()):
            yield KVPValue(k, v)


class KVPValue(BaseValue):

    def __init__(self, key, value):
        super(KVPValue, self).__init__(MissingType.instance)
        self.key = TextValue(key)
        self.value = value

    def getMemberValue(self, context, name, autoCreate=False):
        if "key" == name:
            return self.key
        elif "value" == name:
            value = self.value
            if isinstance(value, IExpression):
                value = value.interpret(context)
            return value
        else:
            raise SyntaxError("No such member:" + name)
