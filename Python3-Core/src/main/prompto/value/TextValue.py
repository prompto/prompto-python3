from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.store.InvalidValueError import InvalidValueError
from prompto.type.TextType import TextType
from prompto.value.BaseValue import BaseValue
from prompto.value.IMultiplyable import IMultiplyable
from prompto.value.ISliceable import ISliceable
from prompto.value.IntegerValue import IntegerValue


class TextValue(BaseValue, ISliceable, IMultiplyable):

    def __init__(self, value):
        super(TextValue, self).__init__(TextType.instance)
        self.value = value


    def convertToPython(self):
        return self.value


    def getStorableData(self):
        return self.value


    def getValue(self):
        return self.value


    def size(self):
        return len(self.value)


    def isEmpty(self):
        return len(self.value) == 0


    def Add(self, context, value):
        return TextValue(self.value + str(value))


    def Multiply(self, context, value):
        if isinstance(value, IntegerValue):
            count = value.IntegerValue()
            if count < 0:
                raise SyntaxError("Negative repeat count:" + count)
            if count == 0:
                return TextValue("")
            if count == 1:
                return TextValue(self.value)
            return TextValue(self.value * count)
        else:
            super(TextValue, self).Multiply(context, value)


    def compareTo(self, context, value):
        if isinstance(value, TextValue):
            if self.value < value.value:
                return -1
            elif self.value == value.value:
                return 0
            else:
                return 1
        else:
            super(TextValue, self).CompareTo(context, value)


    def hasItem(self, context, value):
        from prompto.value.CharacterValue import CharacterValue
        if isinstance(value, CharacterValue):
            return self.value.find(value.value) >= 0
        elif isinstance(value, TextValue):
            return self.value.find(value.value) >= 0
        else:
            raise SyntaxError("Illegal contain: Text + " + type(value).__name__)


    def getMemberValue(self, context, name, autoCreate=False):
        if "count" == name:
            return IntegerValue(len(self.value))
        else:
            return super().getMemberValue(context, name, autoCreate)


    def getItem(self, context, index):
        from prompto.value.CharacterValue import CharacterValue
        try:
            if isinstance(index, IntegerValue):
                return CharacterValue(self.value[index.IntegerValue() - 1])
            else:
                raise InvalidValueError("No such item:" + str(index))
        except IndexError:
            raise IndexOutOfRangeError()


    def getIterator(self, context):
        from prompto.value.CharacterValue import CharacterValue
        for c in self.value:
            yield CharacterValue(c)

    def ConvertTo(self, itype):
        return self.value


    def slice(self, fi, li):
        first = self.checkFirst(fi)
        last = self.checkLast(li)
        return TextValue(self.value[first - 1:last])


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
        from prompto.value.CharacterValue import CharacterValue
        if isinstance(value, (CharacterValue, TextValue)):
            if len(self.value)!=len(value.value):
                return False
            return self.value.lower()==value.value.lower()
        else:
            return False


    def Contains(self, context, value):
        from prompto.value.CharacterValue import CharacterValue
        if isinstance(value, (TextValue, CharacterValue)):
            return self.value.index(value.value) >= 0
        else:
            return False


    def __str__(self):
        return self.value


    def __eq__(self, obj):
        if isinstance(obj, TextValue):
            return self.value == obj.value
        else:
            return self.value == obj

    def __lt__(self, other):
        return self.value < str(other)

    def __hash__(self):
        return hash(self.value)

    def toJson(self, context, generator, instanceId, fieldName, withType, binaries):
        generator.writeString(self.value)


    def toJsonNode(self):
        return self.value
