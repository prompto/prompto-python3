from prompto.grammar.NativeCategoryBinding import NativeCategoryBinding


class JavaScriptNativeCategoryBinding(NativeCategoryBinding):

    def __init__(self, identifier, module):
        super(JavaScriptNativeCategoryBinding, self).__init__()
        self.identifier = identifier
        self.module = module

    def toDialect(self, writer):
        writer.append("JavaScript: ")
        writer.append(self.identifier)
        if self.module is not None:
            self.module.toDialect(writer)
