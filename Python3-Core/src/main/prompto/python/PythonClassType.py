from datetime import date, time, datetime, timedelta
from prompto.declaration.AnyNativeCategoryDeclaration import AnyNativeCategoryDeclaration
from prompto.type.CategoryType import CategoryType
from prompto.type.IntegerType import IntegerType
from prompto.type.BooleanType import BooleanType
from prompto.type.DecimalType import DecimalType
from prompto.type.TextType import TextType
from prompto.type.DateType import DateType
from prompto.type.TimeType import TimeType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.PeriodType import PeriodType
from prompto.type.AnyType import AnyType
from prompto.value.IValue import IValue
from prompto.value.Period import Period
from prompto.error.InternalError import InternalError


class PythonClassType(CategoryType):
    pythonToPrestoMap = { bool.__name__: BooleanType.instance,
                         int.__name__: IntegerType.instance,
                         float.__name__: DecimalType.instance,
                         str.__name__: TextType.instance,
                         date.__name__: DateType.instance,
                         time.__name__: TimeType.instance,
                         datetime.__name__: DateTimeType.instance,
                         timedelta.__name__: PeriodType.instance,
                         Period.__name__: PeriodType.instance,
                         object.__name__: AnyType.instance
                        }


    def __init__(self, klass):
        super(PythonClassType, self).__init__(klass.__name__)
        self.klass = klass

    def convertPythonTypeToPrestoType(self):
        result = PythonClassType.pythonToPrestoMap.get(self.klass.__name__, None)
        if result is None:
            return self
        else:
            return result

    def convertPythonValueToPrestoValue(self, context, value, returnType):
        from prompto.value.NativeInstance import NativeInstance
        if isinstance(value, IValue):
            return value
        typ = PythonClassType.pythonToPrestoMap.get(self.klass.__name__, None)
        if typ is not None:
            return typ.convertPythonValueToPrestoValue(context, value, returnType)
        decl = context.getNativeBinding(self.klass)
        if decl is not None:
            return NativeInstance(decl, value)
        elif returnType is AnyType.instance:
            return NativeInstance(AnyNativeCategoryDeclaration.instance, value)
        else:
            raise InternalError("Unable to convert:" + type(value).__name__)
