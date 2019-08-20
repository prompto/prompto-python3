from prompto.store.TypeFamily import TypeFamily
from prompto.type.BaseType import BaseType
from prompto.type.IType import IType


class TypeType(BaseType):

    def __init__(self, typ:IType):
        super().__init__(TypeFamily.TYPE)
        self.typ = typ


    def isMoreSpecificThan(self, context, other):
        return False


    def checkMember(self, context, name):
        return self.typ.checkStaticMember(context, name)


    def getMemberMethods(self, context, name):
        return self.typ.getStaticMemberMethods(context, name)

