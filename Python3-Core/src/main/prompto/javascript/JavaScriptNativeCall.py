from prompto.statement.NativeCall import NativeCall
from prompto.type.VoidType import VoidType


class JavaScriptNativeCall (NativeCall):

    def __init__(self, statement):
        super(JavaScriptNativeCall, self).__init__()
        self.statement = statement

    def toDialect(self, writer):
        writer.append("JavaScript: ")
        self.statement.toDialect(writer)

    def check(self, context):
        return VoidType.instance # TODO

    def interpret(self, context):
        raise Exception("Should never get there!")