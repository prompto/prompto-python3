from collections import Iterator

from prompto.error.InternalError import InternalError
from prompto.runtime.BreakResult import BreakResult
from prompto.runtime.TransientVariable import TransientVariable
from prompto.runtime.Variable import Variable
from prompto.statement.BaseStatement import BaseStatement
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.IntegerType import IntegerType
from prompto.value.IIterable import IIterable
from prompto.value.Integer import Integer


class ForEachStatement(BaseStatement):

    def __init__(self, name1, name2, source, statements):
        super(ForEachStatement, self).__init__()
        self.v1 = name1
        self.v2 = name2
        self.source = source
        self.statements = statements


    def check(self, context):
        srcType = self.source.check(context)
        elemType = srcType.checkIterator(context)
        return self.checkItemIterator(elemType, context)


    def checkItemIterator(self, elemType, context):
        child = context.newChildContext()
        itemName = self.v1 if self.v2 == None else self.v2
        child.registerValue(TransientVariable(itemName, elemType))
        if self.v2 is not None:
            child.registerValue(TransientVariable(self.v1, IntegerType.instance))
        return self.statements.check(child, None)


    def interpret(self, context):
        srcType = self.source.check(context)
        elemType = srcType.checkIterator(context)
        return self.interpretItemIterator(elemType, context)


    def interpretItemIterator(self, elemType, context):
        if self.v2 == None:
            return self.interpretItemIteratorNoIndex(elemType, context)
        else:
            return self.interpretItemIteratorWithIndex(elemType, context)


    def interpretItemIteratorNoIndex(self, elemType, context):
        src = self.source.interpret(context)
        iterable = self.getIterable(context, src)
        for item in iterable:
            child = context.newChildContext()
            child.registerValue(TransientVariable(self.v1, elemType))
            child.setValue(self.v1, item)
            value = self.statements.interpret(child)
            if value is BreakResult.instance:
                break
            if value != None:
                return value
        return None


    def interpretItemIteratorWithIndex(self, elemType, context):
        src = self.source.interpret(context)
        iterable = self.getIterable(context, src)
        i = 0
        for item in iterable:
            child = context.newChildContext()
            child.registerValue(TransientVariable(self.v2, elemType))
            child.setValue(self.v2, item)
            child.registerValue(TransientVariable(self.v1, IntegerType.instance))
            i += 1
            child.setValue(self.v1, Integer(i))
            value = self.statements.interpret(child)
            if value is BreakResult.instance:
                break
            if value is not None:
                return value
        return None


    def getIterable(self, context, src):
        if isinstance(src, IIterable):
            return src.getIterator(context)
        elif isinstance(src, list):
            return src
        elif isinstance(src, Iterator):
            return src
        else:
            raise InternalError("Should never get there!")


    def toDialect(self, writer):
        writer = writer.newChildWriter()
        srcType = self.source.check(writer.context)
        elemType = srcType.checkIterator(writer.context)
        itemName = self.v1 if self.v2 is None else self.v2
        writer.context.registerValue(Variable(itemName, elemType))
        if self.v2 is not None:
            writer.context.registerValue(Variable(self.v1, IntegerType.instance))
        super().toDialect(writer)


    def toODialect(self, writer):
        writer.append("for each (")
        writer.append(self.v1)
        if self.v2 is not None:
            writer.append(", ")
            writer.append(self.v2)
        writer.append(" in ")
        self.source.toDialect(writer)
        writer.append(")")
        oneLine = len(self.statements) == 1 and self.statements[0].isSimple()
        if not oneLine:
            writer.append(" {")
        writer.newLine()
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()
        if not oneLine:
            writer.append("}")
            writer.newLine()


    def toEDialect(self, writer):
        writer.append("for each ")
        writer.append(self.v1)
        if self.v2 is not None:
            writer.append(", ")
            writer.append(self.v2)
        writer.append(" in ")
        self.source.toDialect(writer)
        writer.append(":")
        writer.newLine()
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()


    def toMDialect(self, writer):
        writer.append("for ")
        writer.append(self.v1)
        if self.v2 is not None:
            writer.append(", ")
            writer.append(self.v2)
        writer.append(" in ")
        self.source.toDialect(writer)
        writer.append(":")
        writer.newLine()
        writer.indent()
        self.statements.toDialect(writer)
        writer.dedent()


    def canReturn(self):
        return True