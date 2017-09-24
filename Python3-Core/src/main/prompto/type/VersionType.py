from prompto.type.IType import IType
from prompto.type.TimeType import *
from prompto.value.Date import *
from prompto.value.DateRange import *


class VersionType(NativeType):
    instance = None

    def __init__(self):
        super(VersionType, self).__init__(TypeFamily.VERSION)


    def checkCompare(self, context, other):
        if isinstance(other, VersionType):
            return BooleanType.instance
        else:
            return super(VersionType, self).checkCompare(context, other)

    def sort(self, context, source, desc):
        return sorted(source, reverse=desc)


    def toString(self, value):
        return "'" + value.toString() + "'"


VersionType.instance = VersionType()

