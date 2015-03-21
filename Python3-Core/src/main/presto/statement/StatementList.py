from presto.error.NullReferenceError import NullReferenceError
from presto.parser.Dialect import Dialect
from presto.python.PythonNativeCall import Python3NativeCall
from presto.statement.SimpleStatement import SimpleStatement
from presto.type.TypeMap import TypeMap
from presto.type.VoidType import VoidType


class StatementList(list):

    def __init__(self, statement=None):
        super(StatementList, self).__init__()
        if statement != None:
            self.append(statement)

    def check(self, context, nativeOnly=False):
        types = TypeMap()
        for statement in self:
            if nativeOnly and not isinstance(statement, Python3NativeCall):
                continue
            type_ = statement.check(context)
            if type_ != VoidType.instance:
                types[type_.getName()] = type_
        return types.inferType(context)

    def interpret(self, context, nativeOnly=False):
        try:
            return self.doInterpret(context, nativeOnly)
        except ReferenceError:
            raise NullReferenceError()

    def doInterpret(self, context, nativeOnly):
        for statement in self:
            if nativeOnly and not isinstance(statement, Python3NativeCall):
                continue
            context.enterStatement(statement)
            try:
                result = statement.interpret(context)
                if result is not None:
                    return result
            finally:
                context.leaveStatement(statement)
        return None

    def toDialect(self, writer):
        for statement in self:
            statement.toDialect(writer)
            if isinstance(statement, SimpleStatement):
                if writer.dialect is Dialect.O:
                    writer.append(';')
                writer.newLine()
