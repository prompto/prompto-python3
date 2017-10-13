from prompto.statement.SwitchCase import SwitchCase


class AtomicSwitchCase ( SwitchCase ):

    def __init__(self, expression, statements):
        super(AtomicSwitchCase, self).__init__(expression, statements)

    def checkSwitchType(self, context, itype):
        selfType = self.expression.check(context)
        if not itype.isAssignableFrom(context, selfType):
            raise SyntaxError("Cannot assign:" + selfType.getName() + " to:" + itype.getName())

    def matches(self, context, value):
        selfValue = self.expression.interpret(context)
        return value==selfValue

    def caseToEDialect(self, writer):
        writer.append("when ")
        self.expression.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def caseToODialect(self, writer):
        writer.append("case ")
        self.expression.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def caseToMDialect(self, writer):
        self.caseToEDialect(writer)

    def catchToEDialect(self, writer):
        self.caseToEDialect(writer) #  no difference

    def catchToODialect(self, writer):
        writer.append("catch (")
        self.expression.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("} ")

    def catchToMDialect(self, writer):
        writer.append("except ")
        self.expression.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

