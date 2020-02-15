from prompto.error.SyntaxError import SyntaxError
from prompto.value.BaseValue import BaseValue
from prompto.value.IMultiplyable import IMultiplyable
from prompto.value.IntegerValue import IntegerValue



class CharacterValue (BaseValue, IMultiplyable) :

    def __init__(self, value):
        from prompto.type.CharacterType import CharacterType
        super(CharacterValue, self).__init__(CharacterType.instance)
        self.value = value



    def convertToPython(self):
        return self.value



    def getValue(self):
        return self.value



    def getMemberValue(self, context, name, autoCreate=False):
        if "codePoint" == name:
            return IntegerValue(ord(self.value))
        else:
            return super(CharacterValue, self).getMemberValue(context, name, autoCreate)


    def Add(self, context, value):
        from prompto.value.TextValue import TextValue
        return TextValue(self.value + str(value))



    def Multiply(self, context, value):
        from prompto.value.IntegerValue import IntegerValue
        if isinstance(value, IntegerValue):
            from prompto.value.TextValue import TextValue
            count = value.IntegerValue()
            if count < 0:
                raise SyntaxError("Negative repeat count:" + count)
            if count == 0:
                return TextValue("")
            if count == 1:
                return TextValue(self.value)
            return TextValue(self.value * count)
        else:
            raise SyntaxError("Illegal: Character * " + type(value).__name__)
 

    def compareTo(self, context, other):
        if isinstance(other, CharacterValue):
            if self.value < other.value:
                return -1
            elif self.value == other.value:
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Character + " + type(other).__name__)

    
    def ConvertTo(self, itype):
        return self.value
    
    def Roughly(self, context, value):
        from prompto.value.TextValue import TextValue
        if isinstance(value, CharacterValue) or  isinstance(value, TextValue):
            if len(self.value)!=len(value.value):
                return False
            return self.value.tolower()==value.value.tolower()
        else:
            return False

    def __str__(self):
        return self.value
 
    def __eq__(self, obj):
        if isinstance(obj, CharacterValue):
            return self.value == obj.value
        else:
            return False

    def __lt__(self, obj):
        return self.value < obj.value


    def __hash__(self):
        return hash(self.value)