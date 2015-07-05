from prompto.grammar.IDialectElement import IDialectElement


class JavaScriptModule (IDialectElement):
    def __init__(self, identifiers):
        self.identifiers = identifiers

    def toDialect(self, writer):
        writer.append(" from module: ")
        for identifier in self.identifiers:
            if "js" == identifier:
                writer.trimLast(1)
                writer.append('.')
            writer.append(identifier)
            writer.append('/')
        writer.trimLast(1)
