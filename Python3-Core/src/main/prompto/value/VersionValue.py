from prompto.value.BaseValue import BaseValue
from prompto.error.SyntaxError import SyntaxError

class VersionValue (BaseValue):

    @staticmethod
    def Parse(text):
        if text[0]=='v':
            text = text[1:]
        d1 = text.find('.')
        major = int(text[0:d1])
        d2 = text.find('.', d1 + 1)
        minor = int(text[d1 + 1:d2])
        fix = int(text[d2 + 1:])
        return VersionValue(major=major, minor=minor, fix=fix)

    def __init__(self, major=-1, minor=-1, fix=-1):
        from prompto.type.VersionType import VersionType
        super().__init__(VersionType.instance)
        self.major = major
        self.minor = minor
        self.fix = fix

    def compareTo(self, context, value):
        if isinstance(value, VersionValue):
            if self.asInt() < value.asInt():
                return -1
            elif self.asInt() == value.asInt():
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Version - " + type(value).__name__)

    def asInt(self):
        return (self.major << 24) | (self.minor << 16) | self.fix


    def __eq__(self, obj):
        if isinstance(obj, VersionValue):
            return self.asInt() == obj.asInt()
        else:
            return False

    def __lt__(self, other):
        return self.asInt() < other.asInt()

    def __str__(self):
        return str(self.major) + '.' + str(self.minor) + '.' + str(self.fix)

    def __hash__(self):
        return hash(self.asInt())
