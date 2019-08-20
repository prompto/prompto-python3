from antlr4 import ParseTreeWalker
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.parser.EPromptoBuilder import EPromptoBuilder
from prompto.runtime.utils.Out import Out
from prompto.parser.ECleverParser import ECleverParser
from prompto.runtime.Context import Context

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
        self.assertEqual(-8, value.IntegerValue())

    def test2Plus3Minuses(self):
        exp = self.parseExpression("1+2-3+4-5-6")
        context = Context.newGlobalContext()
        value = exp.interpret(context)
        self.assertEqual(-7, value.IntegerValue())

    def test1Star1Plus(self):
        exp = self.parseExpression("1*2+3")
        context = Context.newGlobalContext()
        value = exp.interpret(context)
        self.assertEqual(5, value.IntegerValue())

    def parseExpression(self, exp):
        parser = ECleverParser(text=exp)
        parser._input.tokenSource.addLF = False
        tree = parser.expression()
        builder = EPromptoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)
