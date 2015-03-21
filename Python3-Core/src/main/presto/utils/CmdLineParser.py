from antlr4 import *
from antlr4.InputStream import InputStream

from presto.utils.ArgsLexer import ArgsLexer
from presto.utils.ArgsParser import ArgsParser
from presto.utils.ArgsParserListener import ArgsParserListener


def parseCmdLine(input_):
    if input_ is None:
        input_ = ""
    try:
        stream = InputStream(input_)
        lexer = ArgsLexer(input=stream)
        tokens = CommonTokenStream(lexer)
        parser = ArgsParser(tokens)
        tree = parser.parse()
        builder = CmdLineBuilder()
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getCmdLineArgs()
    except RecognitionException as e:
        print(e)
        raise e

class CmdLineBuilder(ArgsParserListener):

    def __init__(self):
        self.args = dict()
        self.values = dict()

    def getCmdLineArgs(self):
        return self.args

    def exitEntry(self, ctx:ArgsParser.EntryContext):
        key = self.values[ctx.key()]
        value = self.values[ctx.value()]
        self.args[key] = value

    def exitKey(self, ctx:ArgsParser.KeyContext):
        self.values[ctx] = ctx.getText()

    def exitSTRING(self, ctx:ArgsParser.STRINGContext):
        self.values[ctx] = ctx.getText()[1:-1]

    def exitELEMENT(self, ctx:ArgsParser.ELEMENTContext):
        self.values[ctx] = ctx.getText()
