from prompto.expression.EqualsExpression import EqualsExpression
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.BooleanType import BooleanType
from prompto.value.Boolean import Boolean
from prompto.error.SyntaxError import SyntaxError

class IfStatement ( BaseStatement ):

    def __init__(self, condition, instructions):
        super(IfStatement, self).__init__()
        self.elements = [IfElement(condition,instructions)]

    def addAdditionals(self, elements):
        self.elements.extend(elements)

    def addAdditional(self, condition, instructions):
        self.elements.append(IfElement(condition,instructions))

    def setFinal(self, instructions):
        self.elements.append(IfElement(None,instructions))

    def check(self, context):
        return self.elements[0].check(context)
        # TODO check consistency with additional elements

    def interpret(self, context):
        for element in self.elements:
            condition = element.getCondition()
            test = Boolean.TRUE if condition is None else condition.interpret(context)
            if isinstance(test, Boolean) and Boolean.TRUE==test:
                return element.interpret(context)
        return None

    def toSDialect(self, writer):
        first = True
        for elem in self.elements:
            if not first:
                writer.append("else ")
            elem.toDialect(writer)
            first = False
        writer.newLine()

    def toODialect(self, writer):
        first = True
        curly = False
        for elem in self.elements:
            if not first:
                if curly:
                    writer.append(" ")
                writer.append("else ")
            curly = len(elem.statements) > 1
            elem.toDialect(writer)
            first = False
        writer.newLine()

    def toEDialect(self, writer):
        first = True
        for elem in self.elements:
            if not first:
                writer.append("else ")
            elem.toDialect(writer)
            first = False
        writer.newLine()


class IfElement ( BaseStatement ):

    def __init__(self, condition, statements):
        super(IfElement, self).__init__()
        self.condition = condition
        self.statements = statements

    def check(self, context):
        cond = self.condition.check(context)
        if cond!=BooleanType.instance:
            raise SyntaxError("Expected a boolean condition!")
        context = self.downCast(context, False)
        return self.statements.check(context, None)

    def interpret(self, context):
        context = self.downCast(context, True)
        return self.statements.interpret(context)

    def downCast(self, context, setValue):
        parent = context
        if isinstance(self.condition, EqualsExpression):
            context = self.condition.downCast(context, setValue)
        context = context if id(parent)!=id(context) else context.newChildContext()
        return context

    def toSDialect(self, writer):
        self.toEDialect(writer)

    def toODialect(self, writer):
        if self.condition is not None:
            writer.append("if (")
            self.condition.toDialect(writer)
            writer.append(") ")
        curly = self.statements is not None and len(self.statements) > 1
        if curly:
            writer.append("{\n")
        else:
            writer.newLine()
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        if curly:
            writer.append("}")

    def toEDialect(self, writer):
        if self.condition is not None:
            writer.append("if ")
            self.condition.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()


class IfElementList(list):

    def __init__(self, elem:IfElement=None):
        super().__init__()
        if elem is not None:
            self.append(elem)

