from prompto.type.VoidType import VoidType
from prompto.error.SyntaxError import SyntaxError

class TypeMap ( dict ):

    def inferType(self, context):
        if len(self)==0:
            return VoidType.instance
        common = None
        # first pass: get less specific type
        for t in self.values():
            if common is None:
                common = t
            elif common.isAssignableFrom(context, t):
                continue
            elif t.isAssignableFrom(context, common):
                common = t
            else:
                raise SyntaxError("Incompatible types: " + common.typeName + " and " + t.typeName)
        # second pass: check compatible
        for t in self.values():
            if not common.isAssignableFrom(context, t):
                raise SyntaxError("Incompatible types: " + common.typeName + " and " + t.typeName)
        return common
