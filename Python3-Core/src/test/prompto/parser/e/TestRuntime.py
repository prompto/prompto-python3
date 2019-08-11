import sys

from antlr4 import ParseTreeWalker

from prompto.param.CategoryParameter import CategoryParameter
from prompto.literal.TextLiteral import TextLiteral
from prompto.parser.ECleverParser import ECleverParser
from prompto.parser.EPromptoBuilder import EPromptoBuilder
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.Context import Context
from prompto.runtime.utils.Out import Out
from prompto.type.TextType import TextType


class TestNative(BaseEParserTest):

    def __init__(self, args=None):
        super(TestNative, self).__init__(args)

    def setUp(self):
        super(TestNative, self).setUp()
        Out.init()

    def tearDown(self):
        Out.restore()
        super(TestNative, self).tearDown()

    def testSystemOutPrint(self):
        parser = ECleverParser(text='print(objects=value,end="")')
        parser._input.tokenSource.addLF = False
        tree = parser.python_statement()
        builder = EPromptoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        statement = builder.getNodeValue(tree)
        context = Context.newGlobalContext()
        arg = CategoryParameter(TextType.instance, "value")
        arg.register(context)
        context.setValue("value", TextLiteral('"test"'))  # StringLiteral trims enclosing quotes
        result = statement.interpret(context, None, None) # no module
        self.assertIsNone(result)
        self.assertEquals("test", Out.read())

    def testReturn(self):
        self.runResource("native/return.pec")
        self.assertEquals(sys.platform, Out.read())

    def testDateTimeTZName(self):
        self.runResource("builtins/dateTimeTZName.pec")
        #String tzName = TimeZone.getTimeZone("UTC").getDisplayName(Locale.ENGLISH)
        #assertEquals("tzName=" + tzName, Out.read())

