from presto.grammar.NativeCategoryMapping import NativeCategoryMapping


class PythonNativeCategoryMapping(NativeCategoryMapping):

    def __init__(self, identifier, module):
        super(PythonNativeCategoryMapping, self).__init__()
        self.identifier = identifier
        self.module = module

    def getIdentifier(self):
        return self.identifier

    def getModule(self):
        return self.module

    def interpret(self):
        m = self.module.resolve()
        if m is None:
            return None
        else:
            return m.__dict__.get(self.identifier, None)

    def toDialect(self, writer):
        writer.append(self.identifier)
        if self.module is not None:
            self.module.toDialect(writer)

class Python2NativeCategoryMapping(PythonNativeCategoryMapping):

    def __init__(self, identifier, module):
        super(Python2NativeCategoryMapping, self).__init__(identifier, module)

    def toDialect(self, writer):
        writer.append("Python2: ")
        super(Python2NativeCategoryMapping, self).toDialect(writer)

class Python3NativeCategoryMapping(PythonNativeCategoryMapping):

    def __init__(self, identifier, module):
        super(Python3NativeCategoryMapping, self).__init__(identifier, module)

    def toDialect(self, writer):
        writer.append("Python3: ")
        super(Python3NativeCategoryMapping, self).toDialect(writer)
