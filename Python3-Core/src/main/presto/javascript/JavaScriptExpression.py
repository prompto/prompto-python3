from presto.grammar.IDialectElement import IDialectElement


class JavaScriptExpression(IDialectElement):

    def toDialect(self, writer):
        raise Exception("Not implemented!")
