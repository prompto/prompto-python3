from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.expression.IExpression import IExpression


class GetterMethodDeclaration(ConcreteMethodDeclaration, IExpression):

    def __init__(self, name, statements):
        super().__init__(name, None, None, statements)

    def checkMember(self, category, context):
        pass  # TODO

    def toMDialect(self, writer):
        writer.append("def ")
        writer.append(self.name)
        writer.append(" getter():\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        writer.append("getter ")
        writer.append(self.name)
        writer.append(" {\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        writer.append("}\n")

    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" as getter doing:\n")
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()

