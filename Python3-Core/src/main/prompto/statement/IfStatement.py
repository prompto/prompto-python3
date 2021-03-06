from prompto.expression.EqualsExpression import EqualsExpression
from prompto.statement.BaseStatement import BaseStatement
from prompto.type.BooleanType import BooleanType
from prompto.type.TypeMap import TypeMap
from prompto.type.VoidType import VoidType
from prompto.value.BooleanValue import BooleanValue
from prompto.error.SyntaxError import SyntaxError

class IfStatement ( BaseStatement ):

    def __init__(self, condition, statements):
        super(IfStatement, self).__init__()
        self.elements = [IfElement(condition, statements)]


    def addAdditionals(self, elements):
        self.elements.extend(elements)


    def addAdditional(self, condition, statements):
        self.elements.append(IfElement(condition, statements))


    def setFinal(self, statements):
        self.elements.append(IfElement(None, statements))


    def check(self, context):
        types = TypeMap()
        for element in self.elements:
            typ = element.check(context)
            if typ is not VoidType.instance:
                types.add(typ)
        return types.inferType(context)


    def interpret(self, context):
        for element in self.elements:
            condition = element.condition
            test = BooleanValue.TRUE if condition is None else condition.interpret(context)
            if isinstance(test, BooleanValue) and BooleanValue.TRUE==test:
                return element.interpret(context)
        return None


    def canReturn(self):
        return True


    def toMDialect(self, writer):
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
        if self.condition is not None:
            cond = self.condition.check(context)
            if cond!=BooleanType.instance:
                raise SyntaxError("Expected a boolean condition!")
            context = self.downcast(context, False)
        return self.statements.check(context, None)


    def interpret(self, context):
        context = self.downcast(context, True)
        return self.statements.interpret(context)


    def downcast(self, context, setValue):
        parent = context
        if isinstance(self.condition, EqualsExpression):
            context = self.condition.downcast(context, setValue)
        context = context if id(parent)!=id(context) else context.newChildContext()
        return context


    def toMDialect(self, writer):
        self.toEDialect(writer)


    def toODialect(self, writer):
        context = writer.context
        if self.condition is not None:
            writer.append("if (")
            self.condition.toDialect(writer)
            writer.append(") ")
            context = self.downcast(context, False)
            if context is not writer.context:
                writer = writer.newChildWriter(context)
        curly = self.needsCurlyBraces()
        if curly:
            writer.append("{\n")
        else:
            writer.newLine()
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        if curly:
            writer.append("}")


    def needsCurlyBraces(self):
        if self.statements is None:
            return False
        elif len(self.statements) > 1:
            return True
        else:
            return not self.statements[0].isSimple()


    def toEDialect(self, writer):
        context = writer.context
        if self.condition is not None:
            writer.append("if ")
            self.condition.toDialect(writer)
            context = self.downcast(context, False)
            if context is not writer.context:
                writer = writer.newChildWriter(context)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()


class IfElementList(list):

    def __init__(self, elem:IfElement=None):
        super().__init__()
        if elem is not None:
            self.append(elem)

