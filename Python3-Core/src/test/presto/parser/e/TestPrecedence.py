from antlr4 import ParseTreeWalker
from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.parser.EPrestoBuilder import EPrestoBuilder
from presto.runtime.utils.Out import Out
from presto.parser.ECleverParser import ECleverParser
from presto.runtime.Context import Context

class TestPrecedence(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()

    def tearDown(self):
        Out.restore()

    def test3Minuses(self):
        exp = self.parseExpression("1-2-3-4")
        context = Context.newGlobalContext()
        value = exp.interpret(context)
        self.assertEquals(-8, value.IntegerValue())

    def test2Plus3Minuses(self):
        exp = self.parseExpression("1+2-3+4-5-6")
        context = Context.newGlobalContext()
        value = exp.interpret(context)
        self.assertEquals(-7, value.IntegerValue())

    def test1Star1Plus(self):
        exp = self.parseExpression("1*2+3")
        context = Context.newGlobalContext()
        value = exp.interpret(context)
        self.assertEquals(5, value.IntegerValue())

    def parseExpression(self, exp):
        parser = ECleverParser(text=exp)
        parser._input.tokenSource.addLF = False
        tree = parser.expression()
        builder = EPrestoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)
