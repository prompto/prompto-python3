from prompto.runtime.BreakResult import BreakResult
from prompto.type.VoidType import VoidType
from prompto.statement.SimpleStatement import SimpleStatement


class BreakStatement ( SimpleStatement ):

    def __init__(self):
        super(BreakStatement, self).__init__()

    def __str__(self):
        return "break"

    def toDialect(self, writer):
        writer.append("break")

    def __eq__(self, obj):
        return isinstance(obj, BreakStatement)

    def check(self, context):
        return VoidType.instance

    def interpret(self, context):
        return BreakResult.instance
