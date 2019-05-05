from prompto.expression.IExpression import IExpression
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


    def setExpression(self, expression):
        from prompto.statement.ReturnStatement import ReturnStatement
        stmt = ReturnStatement(expression)
        from prompto.statement.StatementList import StatementList
        self.statements = StatementList(stmt)


    def getSortKeyReader(self, context, itemType):
        if len(self.args) == 1:
            return self.getSortKeyReader1Arg(context, itemType)
        elif len(self.args) == 2:
            return self.getSortKeyReader2Args(context, itemType)


    def getSortKeyReader1Arg(self, context, itemType):

        local = self.registerArrowArgs(context.newLocalContext(), itemType)
        def keyGetter(o):
            local.setValue(self.args[0], o)
            return self.statements.interpret(local)

        return keyGetter


    def getSortKeyReader2Args(self, context, itemType):
        local = self.registerArrowArgs(context.newLocalContext(), itemType)
        return lambda o: ItemProxy(local, o, self)


    def registerArrowArgs(self, context, itemType):
        for arg in self.args:
            context.registerValue(Variable(arg, itemType))
        return context


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


