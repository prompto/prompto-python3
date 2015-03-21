from presto.parser.Dialect import Dialect

class IDialectElement(object):

    def toDialect(self, writer):
        if writer.dialect is Dialect.E:
            self.toEDialect(writer)
        elif writer.dialect is Dialect.O:
            self.toODialect(writer)
        elif writer.dialect is Dialect.P:
            self.toPDialect(writer)
        else:
            raise Exception("Unsupported dialect:" + str(writer.dialect))

    def toEDialect(self, writer):
        raise Exception("You must override toEDialect in " + type(self).__name__)

    def toODialect(self, writer):
        raise Exception("You must override toODialect in " + type(self).__name__)

    def toPDialect(self, writer):
        raise Exception("You must override toPDialect in " + type(self).__name__)