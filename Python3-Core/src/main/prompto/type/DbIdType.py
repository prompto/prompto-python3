from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class DbIdType ( NativeType ):

    instance = None

    def __init__(self):
        super(DbIdType, self).__init__(TypeFamily.DBID)
        self.typeName = "DbId"

    def isAssignableFrom(self, context, other):
        return isinstance(other, NativeType)

DbIdType.instance = DbIdType()