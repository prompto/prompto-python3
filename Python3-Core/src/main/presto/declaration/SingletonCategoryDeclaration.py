from presto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration

class SingletonCategoryDeclaration(ConcreteCategoryDeclaration):

    def __init__(self, name, attributes, methods):
        super().__init__(name, attributes)
        self.setMethods(methods)

    def categoryTypeToEDialect(self, writer):
        writer.append("singleton")

    def categoryTypeToODialect(self, writer):
        writer.append("singleton")

    def categoryTypeToPDialect(self, writer):
        writer.append("singleton")
