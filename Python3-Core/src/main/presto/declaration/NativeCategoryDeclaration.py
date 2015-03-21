from presto.declaration.CategoryDeclaration import CategoryDeclaration
from presto.value.NativeInstance import NativeInstance
from presto.error.SyntaxError import SyntaxError
from presto.python.PythonNativeCategoryMapping import Python3NativeCategoryMapping

class NativeCategoryDeclaration ( CategoryDeclaration ):

    def __init__(self, name, attributes, categoryMappings, attributeMappings):
        super(NativeCategoryDeclaration, self).__init__(name, attributes)
        self.categoryMappings = categoryMappings
        self.attributeMappings = attributeMappings
        self.mappedClass = None

    def __str__(self):
        return self.getName() + (":" + str(self.attributes)) if self.attributes is not None else ""

    def newInstance(self):
        return NativeInstance(self)

    def getMappedClass(self):
        if self.mappedClass is None:
            mapping = self.getMapping()
            self.mappedClass = mapping.interpret()
            if self.mappedClass is None:
                raise SyntaxError("No Python class:" + str(mapping))
        return self.mappedClass

    def getMapping(self):
        for mapping in self.categoryMappings:
            if isinstance(mapping, Python3NativeCategoryMapping):
                return mapping
        raise SyntaxError("Missing PYTHON3 mapping !")

    def toEDialect(self, writer):
        self.protoToEDialect(writer, False, True)
        self.mappingsToEDialect(writer)


    def categoryTypeToEDialect(self, writer):
        writer.append("native category")

    def mappingsToEDialect(self, writer):
        writer.indent()
        self.categoryMappings.toDialect(writer)
        writer.dedent()
        writer.newLine()

    def toODialect(self, writer):
        self.allToODialect(writer, True) # always has body;

    def categoryTypeToODialect(self, writer):
        writer.append("native category")

    def bodyToODialect(self, writer):
        self.categoryMappings.toDialect(writer)

    def toPDialect(self, writer):
        self.protoToPDialect(writer, None)
        writer.indent()
        writer.newLine()
        self.categoryMappings.toDialect(writer)
        writer.dedent()
        writer.newLine()

    def categoryTypeToPDialect(self, writer):
        writer.append("native category")
