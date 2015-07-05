from prompto.statement.BaseSwitchStatement import BaseSwitchStatement


class SwitchStatement(BaseSwitchStatement):

    def __init__(self, expression):
        super(SwitchStatement, self).__init__()
        self.expression = expression

    def checkSwitchType(self, context):
        return self.expression.check(context)

    def interpret(self, context):
        switchValue = self.expression.interpret(context)
        return self.interpretSwitch(context, switchValue, None)

    def toSDialect(self, writer):
        self.toEDialect(writer)

    def toODialect(self, writer):
        writer.append("switch(")
        self.expression.toDialect(writer)
        writer.append(") {\n")
        for sc in self.switchCases:
            sc.caseToODialect(writer)
        if self.defaultCase is not None:
            writer.append("default:\n")
            writer.indent()
            self.defaultCase.toDialect(writer)
            writer.dedent()
        writer.append("}\n")

    def toEDialect(self, writer):
        writer.append("switch on ")
        self.expression.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        for sc in self.switchCases:
            sc.caseToEDialect(writer)
        if self.defaultCase is not None:
            writer.append("otherwise:\n")
            writer.indent()
            self.defaultCase.toDialect(writer)
            writer.dedent()
        writer.dedent()

