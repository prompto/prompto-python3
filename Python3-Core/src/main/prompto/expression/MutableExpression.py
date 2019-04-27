from prompto.expression.IExpression import IExpression
from prompto.type.CategoryType import CategoryType
from prompto.error.SyntaxError import SyntaxError
from prompto.value.IInstance import IInstance
from prompto.value.NullValue import NullValue


class MutableExpression(IExpression):

    def __init__(self, source:IExpression):
        self.source = source


    def check(self, context):
        sourceType = self.source.check(context)
        if not isinstance(sourceType, CategoryType):
            raise SyntaxError("Expected a category instance, got:" + str(sourceType))
        return CategoryType(sourceType.typeName, mutable=True)


    def interpret(self, context):
        value = self.source.interpret(context)
        if value is None or value is NullValue.instance:
            return value
        elif isinstance(value, IInstance):
            return value.toMutable()
        else:
            raise SyntaxError("Expected a category instance, got:" + str(value))


    def toDialect(self, writer):
        writer.append("mutable ")
        self.source.toDialect(writer)