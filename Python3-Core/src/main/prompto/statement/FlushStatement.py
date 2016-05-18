from prompto.parser.Dialect import Dialect
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.store.Store import Store
from prompto.type.VoidType import VoidType


class FlushStatement(SimpleStatement):


    def check(self, context):
        return VoidType.instance


    def interpret(self, context):
        Store.instance.flush()


    def toDialect(self, writer):
        writer.append("flush")
        if writer.dialect is not Dialect.E:
            writer.append("()")
