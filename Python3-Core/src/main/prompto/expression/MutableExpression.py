from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.IExpression import IExpression
from prompto.type.CategoryType import CategoryType


class MutableExpression(IExpression):

    def __init__(self, source:IExpression):
        self.source = source


    def check(self, context):
        sourceType = self.source.check(context)
        if not isinstance(sourceType, CategoryType):
            raise SyntaxError("Expected a category instance, got:" + str(sourceType))
        return CategoryType(sourceType.typeName, mutable=True)


    def interpret(self, context):
        sourceType = self.check(context)
        ctor = ConstructorExpression(sourceType, self.source, None, True)
        return ctor.interpret(context)


    def toDialect(self, writer):
        writer.append("mutable ")
        self.source.toDialect(writer)