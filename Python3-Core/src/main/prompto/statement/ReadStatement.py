from prompto.expression.ReadAllExpression import ReadAllExpression
from prompto.type.TextType import TextType


class ReadStatement(ReadAllExpression):

    def __init__(self, source, thenWith):
        super().__init__(source)
        self.thenWith = thenWith


    def canReturn(self):
        return False


    def isSimple(self):
        return False


    def check(self, context):
        super().check(context)
        self.thenWith.check(context, TextType.instance)


    def interpret(self, context):
        record = super().interpret(context)
        self.thenWith.interpret(context, record)


    def toDialect(self, writer):
        super().toDialect(writer)
        self.thenWith.toDialect(writer, TextType.instance)

