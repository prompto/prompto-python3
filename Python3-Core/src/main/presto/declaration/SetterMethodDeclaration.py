from presto.declaration.BaseCategoryMethodDeclaration import BaseCategoryMethodDeclaration
from presto.expression.IExpression import IExpression


class SetterMethodDeclaration(BaseCategoryMethodDeclaration, IExpression):

    def __init__(self, name, instructions):
        super(SetterMethodDeclaration, self).__init__(name, None, instructions)

    def checkMember(self, category, context):
        pass  # TODO

    def toPDialect(self, writer):
        writer.append("def ")
        writer.append(self.name)
        writer.append(" setter():\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()

    def toODialect(self, writer):
        writer.append("setter ")
        writer.append(self.name)
        writer.append(" {\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()
        writer.append("}\n")

    def toEDialect(self, writer):
        writer.append("define ")
        writer.append(self.name)
        writer.append(" setter doing:\n")
        writer.indent()
        self.instructions.toDialect(writer)
        writer.dedent()

