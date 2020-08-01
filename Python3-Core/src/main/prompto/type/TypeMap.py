from prompto.type.NullType import NullType
from prompto.type.VoidType import VoidType
from prompto.error.SyntaxError import SyntaxError

class TypeMap ( dict ):

    def inferType(self, context):
        if len(self)==0:
            return VoidType.instance
        inferred = None
        # first pass: get less specific type
        for t in self.values():
            if t is NullType.instance:
                continue
            elif inferred is None:
                inferred = t
            elif inferred.isAssignableFrom(context, t):
                continue
            elif t.isAssignableFrom(context, inferred):
                inferred = t
            else:
                raise SyntaxError("Incompatible types: " + inferred.typeName + " and " + t.typeName)
        if inferred is None:
            return NullType.instance
        # second pass: check compatible
        for t in self.values():
            if not inferred.isAssignableFrom(context, t):
                raise SyntaxError("Incompatible types: " + inferred.typeName + " and " + t.typeName)
        return inferred
