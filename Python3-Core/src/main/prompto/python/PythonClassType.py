from datetime import date, time, datetime, timedelta

from collections import Iterator

from prompto.declaration.AnyNativeCategoryDeclaration import AnyNativeCategoryDeclaration
from prompto.type.CategoryType import CategoryType
from prompto.type.DocumentType import DocumentType
from prompto.type.IntegerType import IntegerType
from prompto.type.DecimalType import DecimalType
from prompto.type.IteratorType import IteratorType
from prompto.type.SetType import SetType
from prompto.type.TextType import TextType
from prompto.type.DateType import DateType
from prompto.type.ListType import ListType
from prompto.type.TimeType import TimeType
from prompto.type.DateTimeType import DateTimeType
from prompto.type.PeriodType import PeriodType
from prompto.type.AnyType import AnyType
from prompto.value.Document import Document
from prompto.value.IteratorValue import IteratorValue
from prompto.value.ListValue import ListValue
from prompto.value.IValue import IValue
from prompto.value.Period import Period
from prompto.error.InternalError import InternalError
from prompto.value.SetValue import SetValue


class PythonClassType(CategoryType):
    from prompto.type.BooleanType import BooleanType
    pythonToPromptoMap = { bool.__name__: BooleanType.instance,
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
        result = PythonClassType.pythonToPromptoMap.get(self.klass.__name__, None)
        if result is None:
            return self
        else:
            return result

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        return self.doConvertPythonValueToPromptoValue(context, value, self.klass, returnType)

    def doConvertPythonValueToPromptoValue(self, context, value, klass, returnType):
        res = self.convertIValue(value)
        if res is not None:
            return res
        else:
            res = self.convertNative(context, value, klass, returnType)
        if res is not None:
            return res
        else:
            res = self.convertDocument(context, value, klass, returnType)
        if res is not None:
            return res
        else:
            res = self.convertList(context, value, klass, returnType)
        if res is not None:
            return res
        else:
            res = self.convertSet(context, value, klass, returnType)
        if res is not None:
            return res
        else:
            res = self.convertDict(context, value, klass, returnType)
        if res is not None:
            return res
        else:
            res = self.convertIterator(context, value, klass, returnType)
        if res is not None:
            return res
        else:
            res = self.convertCategory(context, value, klass, returnType)
        if res is not None:
            return res
        elif returnType is AnyType.instance:
            from prompto.value.NativeInstance import NativeInstance
            return NativeInstance(AnyNativeCategoryDeclaration.instance, value)
        else:
            raise InternalError("Unable to convert:" + type(value).__name__)

    def convertCategory(self, context, value, klass, returnType):
        from prompto.value.NativeInstance import NativeInstance
        decl = context.getNativeBinding(klass)
        if decl is not None:
            return NativeInstance(decl, value)
        else:
            return None

    def convertIterator(self, context, value, klass, returnType):
        if isinstance(returnType, IteratorType) and isinstance(value, Iterator):
            # need a function because Python won't allow yield and return in the same body
            generator = self.makeGenerator(context, value, klass, returnType)
            return IteratorValue(returnType.itemType, generator)
        else:
            return None


    def makeGenerator(self, context, value, klass, returnType):
        itemType = returnType.itemType
        for item in value:
            ivalue = self.doConvertPythonValueToPromptoValue(context, item, type(item), itemType)
            yield ivalue


    def convertDict(self, context, value, klass, returnType):
        return None # TODO


    def convertSet(self, context, value, klass, returnType):
        if isinstance(returnType, SetType) and isinstance(value, set):
            itemType = returnType.itemType
            itemKlass = type(value[0]) if len(value)>0 else None
            items = [self.doConvertPythonValueToPromptoValue(context, item, itemKlass, itemType) for item in value]
            return SetValue(itemType, items=items)
        else:
            return None

    def convertList(self, context, value, klass, returnType):
        if isinstance(returnType, ListType) and isinstance(value, list):
            itemType = returnType.itemType
            itemKlass = type(value[0]) if len(value)>0 else None
            items = [self.doConvertPythonValueToPromptoValue(context, item, itemKlass, itemType) for item in value]
            return ListValue(itemType, items=items)
        else:
            return None

    def convertDocument(self, context, value, klass, returnType):
        if isinstance(returnType, DocumentType) and isinstance(value, dict):
            doc = Document()
            for key, val in value.items():
                klass = type(val)
                itype = self.pythonToPromptoMap.get(klass.__name__, DocumentType.instance)
                if itype is not None:
                    ival = itype.convertPythonValueToPromptoValue(context, val, None)
                else:
                    ival = self.doConvertPythonValueToPromptoValue(context, val, klass, itype)
                doc.SetMember(context, str(key), ival)
            return doc
        else:
            return None

    def convertNative(self, context, value, klass, returnType):
        typ = PythonClassType.pythonToPromptoMap.get(klass.__name__, None)
        if typ is not None:
            return typ.convertPythonValueToPromptoValue(context, value, returnType)
        else:
            return None

    def convertIValue(selfself, value):
        if isinstance(value, IValue):
            return value
        else:
            return None