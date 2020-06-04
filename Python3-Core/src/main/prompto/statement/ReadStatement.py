from prompto.expression.ReadAllExpression import ReadAllExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Variable import Variable
from prompto.type.TextType import TextType
from prompto.type.VoidType import VoidType


class ReadStatement(ReadAllExpression):

    def __init__(self, source, name, stmts):
        super().__init__(source)
        self.name = name
        self.stmts = stmts


    def canReturn(self):
        return False


    def isSimple(self):
        return False


    def check(self, context):
        super().check(context)
        context = context.newChildContext()
        context.registerValue(Variable(self.name, TextType.instance))
        self.stmts.check(context, None)
        return VoidType.instance


    def interpret(self, context):
        record = super().interpret(context)
        context = context.newChildContext()
        context.registerValue(Variable(self.name, TextType.instance))
        context.setValue(self.name, record)
        self.stmts.interpret(context)
        return None


    def toDialect(self, writer):
        super().toDialect(writer)
        writer.append(" then with ").append(self.name)
        if writer.dialect is Dialect.O:
            writer.append(" {")
        else:
            writer.append(":")
        writer = writer.newChildWriter()
        writer.context.registerValue(Variable(self.name, TextType.instance))
        writer.newLine().indent()
        self.stmts.toDialect(writer)
        writer.dedent()
        if writer.dialect is Dialect.O:
            writer.append("}")

