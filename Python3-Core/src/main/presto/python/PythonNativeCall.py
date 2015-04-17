from presto.statement.NativeCall import NativeCall

class PythonNativeCall(NativeCall):

    def __init__(self, statement, module):
        super(PythonNativeCall, self).__init__()
        self.statement = statement
        self.module = module

    def __str__(self):
        return str(self.statement)

    def check(self, context):
        return self.statement.check(context)

    def interpret(self, context, returnType):
        return self.statement.interpret(context, self.module, returnType)

    def toDialect(self, writer):
        self.statement.toDialect(writer)
        if self.module is not None:
            self.module.toDialect(writer)

class Python2NativeCall(PythonNativeCall):

    def __init__(self, statement, module):
        super(Python2NativeCall, self).__init__(statement, module)

    def toDialect(self, writer):
        writer.append("Python2: ")
        super(Python2NativeCall, self).toDialect(writer)

class Python3NativeCall(PythonNativeCall):

    def __init__(self, statement, module):
        super(Python3NativeCall, self).__init__(statement, module)

    def toDialect(self, writer):
        writer.append("Python3: ")
        super(Python3NativeCall, self).toDialect(writer)
