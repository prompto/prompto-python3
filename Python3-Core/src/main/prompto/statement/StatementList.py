from prompto.error.NullReferenceError import NullReferenceError
from prompto.parser.Dialect import Dialect
from prompto.python.PythonNativeCall import Python3NativeCall
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.TypeMap import TypeMap
from prompto.type.VoidType import VoidType


class StatementList(list):

    def __init__(self, statement=None):
        super(StatementList, self).__init__()
        if statement != None:
            self.append(statement)

    def check(self, context, returnType, nativeOnly=False):
        if returnType == VoidType.instance:
            for statement in self:
                if nativeOnly and not isinstance(statement, Python3NativeCall):
                    continue
                type_ = statement.check(context)
                if type_ != VoidType.instance:
                    raise SyntaxError("Illegal return!")
        else:
            types = TypeMap()
            if returnType is not None:
                types[returnType.getName()] = returnType
            for statement in self:
                if nativeOnly and not isinstance(statement, Python3NativeCall):
                    continue
                type_ = statement.check(context)
                if type_ != VoidType.instance:
                    types[type_.getName()] = type_
            type_ = types.inferType(context)
            if returnType is not None:
                return returnType
            else:
                return type_

    def interpret(self, context):
        try:
            return self.doInterpret(context)
        except ReferenceError:
            raise NullReferenceError()

    def interpretNative(self, context, returnType):
        try:
            return self.doInterpretNative(context, returnType)
        except ReferenceError:
            raise NullReferenceError()

    def doInterpret(self, context):
        for statement in self:
            context.enterStatement(statement)
            try:
                result = statement.interpret(context)
                if result is not None:
                    return result
            finally:
                context.leaveStatement(statement)
        return None

    def doInterpretNative(self, context, returnType):
        for statement in self:
            if not isinstance(statement, Python3NativeCall):
                continue
            context.enterStatement(statement)
            try:
                result = statement.interpret(context, returnType)
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
