from prompto.expression.FetchOneExpression import FetchOneExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Variable import Variable
from prompto.type.VoidType import VoidType


class FetchOneStatement(FetchOneExpression):

    def __init__(self, typ, predicate, name, stmts):
        super().__init__(typ, predicate)
        self.name = name
        self.stmts = stmts


    def canReturn(self):
        return False


    def isSimple(self):
        return False


    def check(self, context):
        super().check(context)
        context = context.newChildContext()
        context.registerValue(Variable(self.name, self.typ))
        self.stmts.check(context, None)
        return VoidType.instance


    def interpret(self, context):
        record = super().interpret(context)
        context = context.newChildContext()
        context.registerValue(Variable(self.name, self.typ))
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
        writer.context.registerValue(Variable(self.name, self.typ))
        writer.newLine().indent()
        self.stmts.toDialect(writer)
        writer.dedent()
        if writer.dialect is Dialect.O:
            writer.append("}")

