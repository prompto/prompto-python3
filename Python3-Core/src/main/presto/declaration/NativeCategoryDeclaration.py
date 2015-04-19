from presto.declaration.CategoryDeclaration import CategoryDeclaration
from presto.error.SyntaxError import SyntaxError

class NativeCategoryDeclaration ( CategoryDeclaration ):

    def __init__(self, name, attributes, categoryMappings, attributeMappings):
        super(NativeCategoryDeclaration, self).__init__(name, attributes)
        self.categoryMappings = categoryMappings
        self.attributeMappings = attributeMappings
        self.mappedClass = None

    def __str__(self):
        return self.getName() + (":" + str(self.attributes)) if self.attributes is not None else ""

    def register(self, context):
        context.registerDeclaration(self)
        mapped = self.getMappedClass(False)
        if mapped is not None:
            context.registerNativeMapping(mapped, self)

    def newInstance(self):
        from presto.value.NativeInstance import NativeInstance
        return NativeInstance(self)

    def getMappedClass(self, fail:bool):
        if self.mappedClass is None:
            mapping = self.getMapping(fail)
            if mapping is not None:
                self.mappedClass = mapping.interpret()
                if fail and self.mappedClass is None:
                    raise SyntaxError("No Python class:" + str(mapping))
        return self.mappedClass

    def getMapping(self, fail:bool):
        for mapping in self.categoryMappings:
            from presto.python.PythonNativeCategoryMapping import Python3NativeCategoryMapping
            if isinstance(mapping, Python3NativeCategoryMapping):
                return mapping
        if fail:
            raise SyntaxError("Missing PYTHON2 mapping !")
        else:
            return None

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
