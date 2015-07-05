from prompto.grammar.IDialectElement import IDialectElement
from prompto.parser.Dialect import Dialect
from prompto.utils.ObjectList import ObjectList


class IdentifierList(ObjectList, IDialectElement):

    @staticmethod
    def parse(ids):
        parts = ids.split(",")
        result = IdentifierList()
        for part in parts:
            result.append(part)
        return result

    def __init__(self, item=None):
        super(IdentifierList, self).__init__()
        if item is not None:
            self.append(item)

    def toDialect(self, writer, finalAnd = False):
        if writer.dialect is Dialect.E:
            self.toEDialect(writer, finalAnd)
        elif writer.dialect is Dialect.O:
            self.toODialect(writer)
        elif writer.dialect is Dialect.S:
            self.toSDialect(writer)
        else:
            raise Exception("Unsupported dialect:" + str(writer.dialect))

    def toEDialect(self, writer, finalAnd):
        if len(self)==1:
            writer.append(self[0])
        elif len(self)>1:
            last = self[-1]
            for s in self:
                if finalAnd and s is last:
                    break
                writer.append(s)
                writer.append(", ")
            writer.trimLast(2)
            if finalAnd:
                writer.append(" and ")
                writer.append(last)

    def toODialect(self, writer):
        if len(self)>0:
            for s in self:
                writer.append(s)
                writer.append(", ")
            writer.trimLast(2)

    def toSDialect(self, writer):
        self.toODialect(writer)
