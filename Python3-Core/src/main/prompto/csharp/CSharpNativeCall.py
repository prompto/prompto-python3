from prompto.statement.NativeCall import NativeCall


class CSharpNativeCall ( NativeCall ):

    def __init__(self, statement):
        super(CSharpNativeCall, self).__init__()
        self.statement = statement

    def __str__(self):
        return str(self.statement)

    def toDialect(self, writer):
        writer.append("C#: ")
        self.statement.toDialect(writer)
