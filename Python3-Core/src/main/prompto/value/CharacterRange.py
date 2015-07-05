from prompto.error.IndexOutOfRangeError import *
from prompto.value.Character import *
from prompto.value.Range import *


class CharacterRange(Range):

    def __init__(self, left, right):
        from prompto.type.CharacterType import CharacterType
        super(CharacterRange, self).__init__(CharacterType.instance, left, right)

    def size(self):
        return 1 + ord(self.high.getValue()[0]) - ord(self.low.getValue()[0])

    def compare(self, o1, o2):
        if o1.value < o2.value:
            return -1
        elif o1.value == o2.value:
            return 0
        else:
            return 1

    def computeItem(self, index):
        result = chr(ord(self.low.getValue()[0]) + index - 1)
        if result > self.high.getValue():
            raise IndexOutOfRangeError()
        return Character(result)

    def newInstance(self, left, right):
        return CharacterRange(left, right)
