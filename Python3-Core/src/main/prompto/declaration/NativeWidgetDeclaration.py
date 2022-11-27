from prompto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration


class NativeWidgetDeclaration(NativeCategoryDeclaration):

    def __init__(self,name, categoryBindings, methods):
        super().__init__(name, None, categoryBindings, None, methods)
        self.properties = None

    def isAWidget(self, context):
        return True

    def asWidget(self, context):
        return self

    def categoryTypeToEDialect(self, writer):
        writer.append("native widget")

    def categoryTypeToODialect(self, writer):
        writer.append("native widget")

    def categoryTypeToMDialect(self, writer):
        writer.append("native widget")
