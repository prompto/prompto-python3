from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import Context
from prompto.runtime.Variable import Variable
from prompto.error.SyntaxError import SyntaxError
from functools import total_ordering

from prompto.utils.CodeWriter import CodeWriter
from prompto.value.Integer import Integer


class ArrowExpression ( IExpression ):

    def __init__(self, args, argsSuite, arrowSuite):
        self.args = args
        self.argsSuite = argsSuite
        self.arrowSuite = arrowSuite
        self.statements = None


    def __str__(self):
        return self.toString(Context.newGlobalContext())


    def toString(self, context: Context):
        try:
            writer = CodeWriter(Dialect.E, context)
            self.toDialect(writer)
            return writer.__str__()
        except:
            return ""


    def interpret(self, context):
        return self.statements.interpret(context)


    def setExpression(self, expression):
        from prompto.statement.ReturnStatement import ReturnStatement
        stmt = ReturnStatement(expression)
        from prompto.statement.StatementList import StatementList
        self.statements = StatementList(stmt)


    def getFilter(self, context, itemType):
        from prompto.value.Boolean import Boolean
        if len(self.args) != 1:
            raise SyntaxError("Expecting 1 parameter only!")
        local = self.registerArrowArgs(context.newLocalContext(), itemType)
        def filter(o):
            local.setValue(self.args[0], o)
            result = self.statements.interpret(local)
            if isinstance(result, Boolean):
                return result.value
            else:
                raise SyntaxError("Expecting a Boolean result!")
        return filter


    def registerArrowArgs(self, context, itemType):
        for arg in self.args:
            context.registerValue(Variable(arg, itemType))
        return context


    def filterToDialect(self, writer, source):
        if len(self.args) != 1:
            raise SyntaxError("Expecting 1 parameter only!")
        sourceType = source.check(writer.context)
        itemType = sourceType.itemType
        writer = writer.newChildWriter()
        self.registerArrowArgs(writer.context, itemType)
        if writer.dialect in [ Dialect.E, Dialect.M ]:
            source.toDialect(writer)
            writer.append(" filtered where ")
            self.toDialect(writer)
        elif writer.dialect == Dialect.O:
            writer.append("filtered (")
            source.toDialect(writer)
            writer.append(") where (")
            self.toDialect(writer)
            writer.append(")")


    def getSortKeyReader(self, context, itemType):
        if len(self.args) == 1:
            return self.getSortKeyReader1Arg(context, itemType)
        elif len(self.args) == 2:
            return self.getSortKeyReader2Args(context, itemType)
        else:
            raise SyntaxError("Expecting 1 or 2 parameters only!")

    def getSortKeyReader1Arg(self, context, itemType):

        local = self.registerArrowArgs(context.newLocalContext(), itemType)
        def keyGetter(o):
            local.setValue(self.args[0], o)
            return self.statements.interpret(local)

        return keyGetter


    def getSortKeyReader2Args(self, context, itemType):
        local = self.registerArrowArgs(context.newLocalContext(), itemType)
        return lambda o: ItemProxy(local, o, self)


    def toDialect(self, writer:CodeWriter):
        self.argsToDialect(writer)
        writer.append(self.argsSuite)
        writer.append("=>")
        writer.append(self.arrowSuite)
        self.bodyToDialect(writer)


    def bodyToDialect(self, writer:CodeWriter):
        from prompto.statement.ReturnStatement import ReturnStatement
        if len(self.statements) == 1 and isinstance(self.statements[0], ReturnStatement):
            self.statements[0].expression.toDialect(writer)
        else:
            writer.append("{").newLine().indent()
            self.statements.toDialect(writer)
            writer.newLine().dedent().append("}").newLine()


    def argsToDialect(self, writer:CodeWriter):
        if self.args is None or len(self.args) == 0:
            writer.append("()")
        elif len(self.args) == 1:
            writer.append(self.args[0])
        else:
            writer.append("(")
            self.args.toDialect(writer, False)
            writer.append(")")


@total_ordering
class ItemProxy(object):

    def __init__(self, context, value, arrow):
        self.context = context
        self.value = value
        self.arrow = arrow


    def __eq__(self, other):
        self.context.setValue(self.arrow.args[0], self.value)
        self.context.setValue(self.arrow.args[1], other.value)
        result = self.arrow.statements.interpret(self.context)
        if not isinstance(result, Integer):
            raise SyntaxError("Expected an Integer, got a " + result.itype)
        return result.value == 0


    def __lt__(self, other):
        self.context.setValue(self.arrow.args[0], self.value)
        self.context.setValue(self.arrow.args[1], other.value)
        result = self.arrow.statements.interpret(self.context)
        if not isinstance(result, Integer):
            raise SyntaxError("Expected an Integer, got a " + result.itype)
        return result.value < 0


