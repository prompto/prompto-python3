from presto.type.VoidType import VoidType


class TypeMap ( dict ):

    def inferType(self, context):
        if len(self)==0:
            return VoidType.instance
        type_ = None
        # first pass: get less specific type
        for t in self.values():
            if type_ is None:
                type_ = t
            elif t.isAssignableTo(context, type_):
                continue
            elif type_.isAssignableTo(context, t):
                type_ = t
            else:
                raise SyntaxError("Incompatible types: " + type_.getName() + " and " + t.getName())
        # second pass: check compatible
        for t in self.values():
            if not t.isAssignableTo(context, type_):
                raise SyntaxError("Incompatible types: " + type_.getName() + " and " + t.getName())
        return type_
