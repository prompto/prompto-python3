from prompto.type.IType import IType
from prompto.type.NullType import NullType
from prompto.type.VoidType import VoidType
from prompto.type.DecimalType import DecimalType
from prompto.error.SyntaxError import SyntaxError

class TypeMap ( dict ):

    def add(self, typ: IType):
        self[typ.typeName] = typ


    def inferType(self, context):
        inferred = None
        # first pass: get less specific type
        for current in self.values():
            if inferred is None or inferred is NullType.instance:
                inferred = current
            elif inferred.isAssignableFrom(context, current):
                inferred = current if current is DecimalType.instance else inferred
            elif current.isAssignableFrom(context, inferred):
                inferred = current
            else:
                common = self.inferCommonBaseType(context, inferred, current)
                if common is not None:
                    inferred = common
                else:
                    raise SyntaxError("Incompatible types: " + inferred.typeName + " and " + current.typeName)
        if inferred is None:
            return VoidType.instance
        # second pass: check compatible
        for current in self.values():
            if not inferred.isAssignableFrom(context, current):
                raise SyntaxError("Incompatible types: " + inferred.typeName + " and " + current.typeName)
        return inferred


    def inferCommonBaseType(self, context, type1, type2):
        from prompto.type.CategoryType import CategoryType
        if isinstance(type1, CategoryType) and isinstance(type2, CategoryType):
            return self.inferCommonCategoryType(context, type1, type2, True)
        else:
            return None


    def inferCommonCategoryType(self, context, type1, type2, trySwap):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.type.CategoryType import CategoryType
        decl1 = context.getRegisteredDeclaration(CategoryDeclaration, type1.typeName)
        if decl1.derivedFrom is not None:
            for name in decl1.derivedFrom:
                parentType = CategoryType(name)
                if parentType.isAssignableFrom(context, type2):
                    return parentType

            # climb up the tree
        for name in decl1.derivedFrom:
            parentType = CategoryType(name)
            commonType = self.inferCommonBaseType(context, parentType, type2)
            if commonType is not None:
                return commonType

        if trySwap:
            return self.inferCommonCategoryType(context, type2, type1, False)
        else:
            return None

