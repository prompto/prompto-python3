from datetime import datetime, timedelta, time, date
from uuid import UUID

from prompto.type.AnyType import AnyType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.DocumentType import DocumentType
from prompto.type.IntegerType import IntegerType
from prompto.type.BooleanType import BooleanType
from prompto.type.MissingType import MissingType
from prompto.type.PeriodType import PeriodType
from prompto.type.TextType import TextType
from prompto.type.TimeType import TimeType
from prompto.type.UUIDType import UUIDType
from prompto.type.VoidType import VoidType
from prompto.error.SyntaxError import SyntaxError

def fieldToValue(context, name, data):
    if data is None:
        return None
    else:
        typ = fieldType(context, name, data)
        return typ.convertPythonValueToPromptoValue(context, data, None)


def fieldType(context, name, data):
    if name=="dbId":
        return typeToIType(type(data))
    else:
        decl = context.getRegisteredDeclaration(name)
        return decl.itype

typeToITypedict = { type(None): VoidType.instance,
                    (bool) : BooleanType.instance,
                    (int) : IntegerType.instance,
                    (float) : DecimalType.instance,
                    (str) : TextType.instance,
                    (UUID) : UUIDType.instance,
                    (date) : DateType.instance ,
                    (time) : TimeType.instance,
                    (datetime) : DateTimeType.instance,
                    (timedelta) : PeriodType.instance,
                    (dict) : DocumentType.instance,
                    (object) : AnyType.instance
                  }

def typeToIType(typ):
    return typeToITypedict.get(typ, None)


def inferElementType(context, expressions):
        if len(expressions)==0:
            return MissingType.instance
        lastType = None
        for o in expressions:
            elemType = o.check(context)
            if lastType is None:
                lastType = elemType
            elif lastType != elemType:
                if lastType.isAssignableFrom(context, elemType):
                    pass  # lastType is less specific
                elif elemType.isAssignableFrom(context, lastType):
                    lastType = elemType  # elemType is less specific
                else:
                    common = inferCommonRootType(context, lastType, elemType)
                    if common is not None:
                        lastType = common
                    else:
                        raise SyntaxError("Incompatible types: " + str(elemType) + " and " + str(lastType))
        return lastType


def inferCommonRootType(context, type1, type2):
    from prompto.type.CategoryType import CategoryType
    if isinstance(type1, CategoryType) and  isinstance(type2, CategoryType):
        return inferCommonCategoryType(context, type1, type2, True)
    else:
        return None


def inferCommonCategoryType(context, type1, type2, trySwap):
    from prompto.declaration.CategoryDeclaration import CategoryDeclaration
    from prompto.type.CategoryType import CategoryType
    decl1 = context.getRegisteredDeclaration(CategoryDeclaration, type1.typeName);
    if decl1.derivedFrom is not None:
        for name in decl1.derivedFrom:
            parentType = CategoryType(name)
            if parentType.isAssignableFrom(context, type2):
                return parentType

        # climb up the tree
    for name in decl1.derivedFrom:
        parentType = CategoryType(name)
        commonType = inferCommonCategoryType(context, parentType, type2, False)
        if commonType is not None:
            return commonType

    if trySwap:
        return inferCommonCategoryType(context, type2, type1, False)
    else:
        return None

