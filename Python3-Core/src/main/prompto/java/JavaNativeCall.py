from prompto.statement.NativeCall import NativeCall


class JavaNativeCall ( NativeCall ):

    def __init__(self, statement):
        super(JavaNativeCall, self).__init__()
        self.statement = statement;

    def __str__(self):
        return str(self.statement)

    def toDialect(self, writer):
        writer.append("Java: ")
        self.statement.toDialect(writer)
