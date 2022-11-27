from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.declaration.ConcreteWidgetDeclaration import ConcreteWidgetDeclaration


class WrappingWidgetDeclaration(ConcreteWidgetDeclaration):

    def __init__(self, wrapped: CategoryDeclaration):
        super().__init__(wrapped.name, wrapped.derivedFrom, wrapped.methods)
