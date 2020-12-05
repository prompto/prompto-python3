from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration

class SingletonCategoryDeclaration(ConcreteCategoryDeclaration):

    def __init__(self, name, attributes, methods):
        super().__init__(name, attributes)
        self.setMethods(methods)

    def categoryTypeToEDialect(self, writer):
        writer.append("singleton")

    def categoryTypeToODialect(self, writer):
        writer.append("singleton")

    def categoryTypeToMDialect(self, writer):
        writer.append("singleton")

    def getInitializeMethod(self, context):
        self.registerMethods(context)
        decl = self.methodsMap.get("initialize", None)
        from prompto.runtime.Context import MethodDeclarationMap
        if isinstance(decl, MethodDeclarationMap):
            method = decl.getFirst()
            from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
            if isinstance(method, ConcreteMethodDeclaration):
                return method
        return None
