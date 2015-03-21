from presto.declaration.NativeCategoryDeclaration import NativeCategoryDeclaration
from presto.runtime.Context import ResourceContext
from presto.type.ResourceType import ResourceType
from presto.value.NativeResource import NativeResource
from presto.error.SyntaxError import SyntaxError


class NativeResourceDeclaration(NativeCategoryDeclaration):

    def __init__(self, name, attributes, categoryMappings, attributeMappings):
        super(NativeResourceDeclaration, self).__init__(name, attributes, categoryMappings, attributeMappings)

    def getType(self, context):
        return ResourceType(self.name)

    def newInstance(self):
        return NativeResource(self)

    def checkConstructorContext(self, context):
        if not isinstance(context, ResourceContext):
            raise SyntaxError("Not a resource context!")

    def categoryTypeToEDialect(self, writer):
        writer.append("native resource")

    def categoryTypeToODialect(self, writer):
        writer.append("native resource")

    def categoryTypeToPDialect(self, writer):
        writer.append("native resource")
