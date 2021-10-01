from prompto.store.TypeFamily import TypeFamily
from prompto.type.NativeType import NativeType


class VersionType(NativeType):
    instance = None

    def __init__(self):
        super(VersionType, self).__init__(TypeFamily.VERSION)


    def checkCompare(self, context, other):
        if isinstance(other, VersionType):
            from prompto.type.BooleanType import BooleanType
            return BooleanType.instance
        else:
            return super(VersionType, self).checkCompare(context, other)


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        from prompto.type.TextType import TextType
        if "major" == name or "minor" == name or "fix" == name:
            return IntegerType.instance
        elif "qualifier" == name:
            return TextType.instance
        else:
            return super(VersionType, self).checkMember(context, name)

    def toString(self, value):
        return "'" + value.toString() + "'"


VersionType.instance = VersionType()

