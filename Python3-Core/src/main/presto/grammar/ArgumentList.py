from presto.grammar.IDialectElement import IDialectElement
from presto.utils.ObjectList import ObjectList


class ArgumentList ( ObjectList, IDialectElement ):

    def __init__(self, item = None):
        super(ArgumentList, self).__init__()
        if item is not None:
            self.append(item)

    def register(self, context):
        for argument in self:
            argument.register(context)

    def check(self, context):
        for argument in self:
            argument.check(context)

    def find(self, name):
        for argument in self:
            if name==argument.getName():
                return argument
        return None

    def toEDialect(self, writer):
        if len(self)>0:
            last = self[-1]
            writer.append("receiving: ")
            for argument in self:
                if argument is last:
                    break
                argument.toDialect(writer)
                writer.append(", ")
            if len(self)>1:
                writer.trimLast(2)
                writer.append(" and ")
            last.toDialect(writer)
            writer.append(" ")

    def toODialect(self, writer):
        if len(self)>0:
            for argument in self:
                argument.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)

    def toPDialect(self, writer):
        if len(self)>0:
            for argument in self:
                argument.toDialect(writer)
                writer.append(", ")
            writer.trimLast(2)
