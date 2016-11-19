from prompto.statement.SwitchCase import SwitchCase
from prompto.type.ContainerType import ContainerType
from prompto.value.IContainer import IContainer
from prompto.value.ListValue import ListValue


class CollectionSwitchCase ( SwitchCase ):

    def __init__(self, expression, list_):
        super(CollectionSwitchCase, self).__init__(expression,list_)

    def checkSwitchType(self, context, type_):
        selfType = self.expression.check(context)
        if isinstance(selfType, ContainerType):
            selfType = selfType.getItemType()
        if not type_.isAssignableFrom(context, selfType):
            raise SyntaxError("Cannot assign:" + selfType.getName() + " to:" + type_.getName())

    def matches(self, context, value):
        selfValue = self.expression.interpret(context)
        if isinstance(selfValue, IContainer):
            return selfValue.hasItem(context, value)
        return False

    def caseToMDialect(self, writer):
        self.caseToEDialect(writer)

    def caseToODialect(self, writer):
        writer.append("case in ")
        self.expression.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def caseToEDialect(self, writer):
        writer.append("when in ")
        self.expression.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def catchToODialect(self, writer):
        writer.append("catch (")
        self.expression.toDialect(writer)
        writer.append(") {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("} ")

    def catchToMDialect(self, writer):
        writer.append("except in ")
        self.expression.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def catchToEDialect(self, writer):
        self.caseToEDialect(writer) # no difference
