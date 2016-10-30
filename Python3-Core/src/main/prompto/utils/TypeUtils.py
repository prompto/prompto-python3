from datetime import datetime, timedelta, time, date
from uuid import UUID

from prompto.type.AnyType import AnyType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.DateType import DateType
from prompto.type.DecimalType import DecimalType
from prompto.type.DocumentType import DocumentType
from prompto.type.IntegerType import IntegerType
from prompto.type.BooleanType import BooleanType
from prompto.type.PeriodType import PeriodType
from prompto.type.TextType import TextType
from prompto.type.TimeType import TimeType
from prompto.type.UUIDType import UUIDType
from prompto.type.VoidType import VoidType


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
        return decl.typ

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
