from presto.statement.SwitchCase import SwitchCase
from presto.type.CollectionType import CollectionType
from presto.value.IContainer import IContainer
from presto.value.ListValue import ListValue


class CollectionSwitchCase ( SwitchCase ):

    def __init__(self, expression, list_):
        super(CollectionSwitchCase, self).__init__(expression,list_)

    def checkSwitchType(self, context, type_):
        selfType = self.expression.check(context)
        if isinstance(selfType, CollectionType):
            selfType = selfType.getItemType()
        if not selfType.isAssignableTo(context, type_):
            raise SyntaxError("Cannot assign:" + selfType.getName() + " to:" + type_.getName())

    def matches(self, context, value):
        selfValue = self.expression.interpret(context)
        if isinstance(selfValue, IContainer):
            return selfValue.hasItem(context, value)
        elif isinstance(selfValue, ValueList):
            return selfValue.hasItem(context, value)
        return False

    def caseToPDialect(self, writer):
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

    def catchToPDialect(self, writer):
        writer.append("except in ")
        self.expression.toDialect(writer)
        writer.append(":\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def catchToEDialect(self, writer):
        self.caseToEDialect(writer) # no difference
