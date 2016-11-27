from prompto.error.SyntaxError import SyntaxError
from prompto.value.BaseValue import BaseValue
from prompto.value.IMultiplyable import IMultiplyable
from prompto.value.Integer import Integer



class Character ( BaseValue, IMultiplyable) :

    def __init__(self, value):
        from prompto.type.CharacterType import CharacterType
        super(Character, self).__init__(CharacterType.instance)
        self.value = value



    def convertToPython(self):
        return self.value



    def getValue(self):
        return self.value



    def getMemberValue(self, context, name, autoCreate=False):
        if "codePoint" == name:
            return Integer(ord(self.value))
        else:
            return super(Character, self).getMemberValue(context, name, autoCreate)


    def Add(self, context, value):
        from prompto.value.Text import Text
        return Text(self.value + str(value))



    def Multiply(self, context, value):
        from prompto.value.Integer import Integer
        if isinstance(value, Integer):
            from prompto.value.Text import Text
            count = value.IntegerValue()
            if count < 0:
                raise SyntaxError("Negative repeat count:" + count)
            if count == 0:
                return Text("")
            if count == 1:
                return Text(self.value)
            return Text(self.value*count)
        else:
            raise SyntaxError("Illegal: Character * " + type(value).__name__)
 

    def compareTo(self, context, other):
        if isinstance(other, Character):
            if self.value < other.value:
                return -1
            elif self.value == other.value:
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Character + " + type(other).__name__)

    
    def ConvertTo(self, type_):
        return self.value
    
    def Roughly(self, context, value):
        from prompto.value.Text import Text
        if isinstance(value, Character) or  isinstance(value, Text):
            if len(self.value)!=len(value.value):
                return False
            return self.value.tolower()==value.value.tolower()
        else:
            return False

    def __str__(self):
        return self.value
 
    def __eq__(self, obj):
        if isinstance(obj, Character):
            return self.value == obj.value
        else:
            return False

    def __lt__(self, obj):
        return self.value < obj.value


    def __hash__(self):
        return hash(self.value)