from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.expression.IExpression import IExpression


class SetterMethodDeclaration(ConcreteMethodDeclaration, IExpression):

    def __init__(self, name, statements):
        super().__init__(name, None, None, statements)

    def checkMember(self, category, context):
        pass  # TODO

    def toSDialect(self, writer):
        writer.append("def ")
        writer.append(self.name)
        writer.append(" setter():\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        writer.append("setter ")
        writer.append(self.name)
        writer.append(" {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("}\n")

    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" setter doing:\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

