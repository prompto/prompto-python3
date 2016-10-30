from prompto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration
from prompto.runtime.Context import ResourceContext
from prompto.type.ResourceType import ResourceType
from prompto.value.NativeResource import NativeResource
from prompto.error.SyntaxError import SyntaxError


class NativeResourceDeclaration(NativeCategoryDeclaration):

    def __init__(self, name, attributes, categoryBindings, attributeBindings, methods):
        super(NativeResourceDeclaration, self).__init__(name, attributes, categoryBindings, attributeBindings, methods)

    def getType(self, context):
        return ResourceType(self.name)

    def newInstance(self, context):
        return NativeResource(self)

    def checkConstructorContext(self, context):
        if not isinstance(context, ResourceContext):
            raise SyntaxError("Not a resource context!")

    def categoryTypeToEDialect(self, writer):
        writer.append("native resource")

    def categoryTypeToODialect(self, writer):
        writer.append("native resource")

    def categoryTypeToSDialect(self, writer):
        writer.append("native resource")
