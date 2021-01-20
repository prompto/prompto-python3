from prompto.parser.Dialect import Dialect
from prompto.runtime.Variable import Variable
from prompto.type.TextType import TextType
from prompto.type.VoidType import VoidType
from prompto.value.IValue import IValue


class ThenWith(object):

    @staticmethod
    def OrEmpty(tw):
        return ThenWith(None, None) if tw is None else tw


    def __init__(self, name, statements):
        self.name = name
        self.statements = statements


    def check(self, context, typ):
        context = context.newChildContext()
        context.registerValue(Variable(self.name, typ))
        self.statements.check(context, None)
        return VoidType.instance


    def interpret(self, context, value: IValue):
        context = context.newChildContext()
        context.registerValue(Variable(self.name, value.GetType(context)))
        context.setValue(self.name, value)
        self.statements.interpret(context)
        return None


    def toDialect(self, writer, typ):
        writer.append(" then with ").append(self.name)
        if writer.dialect is Dialect.O:
            writer.append(" {")
        else:
            writer.append(":")
        writer = writer.newChildWriter()
        writer.context.registerValue(Variable(self.name, typ))
        writer.newLine().indent()
        self.statements.toDialect(writer)
        writer.dedent()
        if writer.dialect is Dialect.O:
            writer.append("}")
