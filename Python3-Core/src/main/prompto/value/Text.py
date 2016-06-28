from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.error.InvalidDataError import InvalidDataError
from prompto.type.TextType import TextType
from prompto.value.BaseValue import BaseValue
from prompto.value.IMultiplyable import IMultiplyable
from prompto.value.ISliceable import ISliceable
from prompto.value.Integer import Integer


class Text(BaseValue, ISliceable, IMultiplyable):

    def __init__(self, value):
        super(Text, self).__init__(TextType.instance)
        self.value = value

    def convertToPython(self):
        return self.value


    def getValue(self):
        return self.value


    def size(self):
        return len(self.value)


    def isEmpty(self):
        return len(self.value) == 0


    def Add(self, context, value):
        return Text(self.value + str(value))


    def Multiply(self, context, value):
        if isinstance(value, Integer):
            count = value.IntegerValue()
            if count < 0:
                raise SyntaxError("Negative repeat count:" + count)
            if count == 0:
                return Text("")
            if count == 1:
                return Text(self.value)
            return Text(self.value * count)
        else:
            super(Text, self).Multiply(context, value)


    def compareTo(self, context, value):
        if isinstance(value, Text):
            if self.value < value.value:
                return -1
            elif self.value == value.value:
                return 0
            else:
                return 1
        else:
            super(Text, self).CompareTo(context, value)


    def hasItem(self, context, value):
        from prompto.value.Character import Character
        if isinstance(value, Character):
            return self.value.find(value.value) >= 0
        elif isinstance(value, Text):
            return self.value.find(value.value) >= 0
        else:
            raise SyntaxError("Illegal contain: Text + " + type(value).__name__)


    def getMember(self, context, name, autoCreate=False):
        if "count" == name:
            return Integer(len(self.value))
        else:
            raise InvalidDataError("No such member:" + name)


    def getItem(self, context, index):
        from prompto.value.Character import Character
        try:
            if isinstance(index, Integer):
                return Character(self.value[index.IntegerValue() - 1])
            else:
                raise InvalidDataError("No such item:" + str(index))
        except IndexError:
            raise IndexOutOfRangeError()


    def getIterator(self, context):
        from prompto.value.Character import Character
        for c in self.value:
            yield Character(c)

    def ConvertTo(self, type_):
        return self.value


    def slice(self, fi, li):
        first = self.checkFirst(fi)
        last = self.checkLast(li)
        return Text(self.value[first - 1:last])


    def checkFirst(self, fi):
        value = 1 if fi is None else fi.IntegerValue()
        if value < 1 or value > len(self.value):
            raise IndexOutOfRangeError()
        return value


    def checkLast(self, li):
        value = len(self.value) if li is None else li.IntegerValue()
        if value < 0:
            value = len(self.value) + 1 + li.IntegerValue()
        if value < 1 or value > len(self.value):
            raise IndexOutOfRangeError()
        return value

    def Roughly(self, context, value):
        from prompto.value.Character import Character
        if isinstance(value, Character) or  isinstance(value, Text):
            if len(self.value)!=len(value.value):
                return False
            return self.value.lower()==value.value.lower()
        else:
            return False

    def __str__(self):
        return self.value


    def __eq__(self, obj):
        if isinstance(obj, Text):
            return self.value == obj.value
        else:
            return self.value == obj

    def __lt__(self, other):
        return self.value < str(other)

    def __hash__(self):
        return hash(self.value)

    def toJson(self, context, generator, instanceId, fieldName, binaries):
        generator.writeString(self.value)