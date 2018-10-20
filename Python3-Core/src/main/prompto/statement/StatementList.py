from prompto.error.NullReferenceError import NullReferenceError
from prompto.error.SyntaxError import SyntaxError
from prompto.parser.Dialect import Dialect
from prompto.python.PythonNativeCall import Python3NativeCall
from prompto.statement.NativeCall import NativeCall
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.AnyType import AnyType
from prompto.type.TypeMap import TypeMap
from prompto.type.VoidType import VoidType


class StatementList(list):

    def __init__(self, statement=None):
        super(StatementList, self).__init__()
        if statement is not None:
            self.append(statement)


    def check(self, context, returnType):
        return self.checkStatements(context, returnType, False)


    def checkNative(self, context, returnType):
        return self.checkStatements(context, returnType, True)


    def checkStatements(self, context, returnType, nativeOnly):
        if returnType == VoidType.instance:
            for statement in self:
                if nativeOnly and not isinstance(statement, Python3NativeCall):
                    continue
                itype = statement.check(context)
                if itype is not VoidType.instance:
                    raise SyntaxError("Illegal return!")
        else:
            types = TypeMap()
            if returnType is not None:
                types[returnType.typeName] = returnType
            for statement in self:
                if nativeOnly and not isinstance(statement, Python3NativeCall):
                    continue
                itype = statement.check(context)
                if not statement.canReturn():
                    itype = VoidType.instance
                if itype != VoidType.instance:
                    # unless necessary, don't collect AnyType returned by native statement check
                    if len(types) == 0 or itype is not AnyType.instance or not nativeOnly:
                        types[itype.typeName] = itype
            itype = types.inferType(context)
            if returnType is not None:
                return returnType
            else:
                return itype


    def interpret(self, context):
        try:
            return self.doInterpret(context)
        except ReferenceError:
            raise NullReferenceError()

    def doInterpret(self, context):
        for statement in self:
            context.enterStatement(statement)
            try:
                result = statement.interpret(context)
                if not statement.canReturn():
                    result = None
                if result is not None:
                    return result
            finally:
                context.leaveStatement(statement)
        return None

    def interpretNative(self, context, returnType):
        try:
            return self.doInterpretNative(context, returnType)
        except ReferenceError:
            raise NullReferenceError()

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
                if writer.dialect is Dialect.O and not isinstance(statement, NativeCall):
                    writer.append(';')
                writer.newLine()
