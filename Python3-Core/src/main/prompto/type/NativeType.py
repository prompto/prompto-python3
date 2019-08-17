from prompto.type.BaseType import BaseType


class NativeType ( BaseType ):

    ALL = None

    @classmethod
    def getAll(cls):
        if cls.ALL is None:
            from prompto.type.AnyType import AnyType
            from prompto.type.BooleanType import BooleanType
            from prompto.type.CharacterType import CharacterType
            from prompto.type.CodeType import CodeType
            from prompto.type.DateTimeType import DateTimeType
            from prompto.type.DateType import DateType
            from prompto.type.DecimalType import DecimalType
            from prompto.type.DocumentType import DocumentType
            from prompto.type.IntegerType import IntegerType
            from prompto.type.PeriodType import PeriodType
            from prompto.type.TextType import TextType
            from prompto.type.TimeType import TimeType
            from prompto.type.TupleType import TupleType
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


    def __init__(self, family):
        super().__init__(family)


    def checkUnique(self, context):
        pass


    def checkExists(self, context):
        pass


    def isMoreSpecificThan(self, context, other):
        return False


    def getSortKeyReader(self, context, expression):
        from prompto.expression.ArrowExpression import ArrowExpression
        if isinstance(expression, ArrowExpression):
            return expression.getSortKeyReader(context, self)
        else:
            return None

