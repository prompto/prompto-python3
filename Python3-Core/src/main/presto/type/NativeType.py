from presto.type.BaseType import BaseType


class NativeType ( BaseType ):

    ALL = None

    @classmethod
    def getAll(cls):
        if cls.ALL is None:
            from presto.type.AnyType import AnyType
            from presto.type.BooleanType import BooleanType
            from presto.type.CharacterType import CharacterType
            from presto.type.CodeType import CodeType
            from presto.type.DateTimeType import DateTimeType
            from presto.type.DateType import DateType
            from presto.type.DecimalType import DecimalType
            from presto.type.DocumentType import DocumentType
            from presto.type.IntegerType import IntegerType
            from presto.type.PeriodType import PeriodType
            from presto.type.TextType import TextType
            from presto.type.TimeType import TimeType
            from presto.type.TupleType import TupleType
            cls.ALL = [
                AnyType.instance,
                BooleanType.instance,
                IntegerType.instance,
                DecimalType.instance,
                CharacterType.instance,
                TextType.instance,
                CodeType.instance,
                DateType.instance,
                TimeType.instance,
                DateTimeType.instance,
                PeriodType.instance,
                DocumentType.instance,
                TupleType.instance
                ]
        return cls.ALL

    def __init__(self, name):
        super(NativeType, self).__init__(name)

    def checkUnique(self, context):
        pass

    def checkExists(self, context):
        pass

    def isMoreSpecificThan(self, context, other):
        return False

    def isAssignableTo(self, context, other):
        return id(other)==id(self)

