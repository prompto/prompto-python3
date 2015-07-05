from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration


class DeclarationList(list):

    def __init__(self, item=None):
        super().__init__()
        if item is not None:
            self.append(item)

    def register(self, context):
        for declaration in self:
            declaration.register(context)

    def check(self, context):
        for declaration in self:
            declaration.check(context)

    def findMain(self):
        for declaration in self:
            if not isinstance(declaration, ConcreteMethodDeclaration):
                continue
            if not declaration.getName() == "main":
                continue
            # TODO check proto
            return declaration
        return None

    def toDialect(self, writer):
        for declaration in self:
            declaration.toDialect(writer)
            writer.newLine()
