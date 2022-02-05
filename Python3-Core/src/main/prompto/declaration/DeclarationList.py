from prompto.declaration.AttributeDeclaration import AttributeDeclaration
from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from prompto.declaration.BaseMethodDeclaration import BaseMethodDeclaration
from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.declaration.TestMethodDeclaration import TestMethodDeclaration
from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration


class DeclarationList(list):

    def __init__(self, item=None):
        super().__init__()
        if item is not None:
            self.append(item)

    def register(self, context):
        self.registerAttributes(context)
        self.registerCategories(context)
        self.registerEnumerated(context)
        self.registerMethods(context)
        self.registerTests(context)


    def registerAttributes(self, context):
        for declaration in filter(lambda d : isinstance(d, AttributeDeclaration), self):
            declaration.register(context)


    def registerCategories(self, context):
        for declaration in filter(lambda d : isinstance(d, CategoryDeclaration), self):
            declaration.register(context)


    def registerEnumerated(self, context):
        for declaration in filter(lambda d : isinstance(d, EnumeratedNativeDeclaration), self):
            declaration.register(context)


    def registerMethods(self, context):
        for declaration in filter(lambda d : isinstance(d, BaseMethodDeclaration), self):
            declaration.register(context)


    def registerTests(self, context):
        for declaration in filter(lambda d : isinstance(d, TestMethodDeclaration), self):
            declaration.register(context)


    def check(self, context):
        for declaration in self:
            if isinstance(declaration, IMethodDeclaration):
                declaration.checkStart(context)
            else:
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
            if declaration.comments is not None:
                for comment in declaration.comments:
                    comment.toDialect(writer)
            if declaration.annotations is not None:
                for annotation in declaration.annotations:
                    annotation.toDialect(writer)
            declaration.toDialect(writer)
            writer.newLine()
