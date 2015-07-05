from antlr4 import ParseTreeWalker
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.parser.OPromptoBuilder import OPromptoBuilder
from prompto.runtime.utils.Out import Out
from prompto.parser.OCleverParser import OCleverParser
from prompto.runtime.Context import Context
from prompto.grammar.CategoryArgument import CategoryArgument
from prompto.type.TextType import TextType
from prompto.literal.TextLiteral import TextLiteral
import sys

class TestNative(BaseOParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()

    def tearDown(self):
        Out.restore()

    def testSystemOutPrint(self):
        parser = OCleverParser(text = 'print(objects=value,end="")')
        tree = parser.python_statement()
        builder = OPromptoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        statement = builder.getNodeValue(tree)
        context = Context.newGlobalContext()
        arg = CategoryArgument(TextType.instance, "value")
        arg.register(context)
        context.setValue("value", TextLiteral("\"test\"")) # StringLiteral trims enclosing quotes
        result = statement.interpret(context, None, None)
        self.assertIsNone(result)
        self.assertEquals("test", Out.read())

    def testReturnText(self):
        self.runResource("native/return.poc")
        self.assertEquals(sys.platform, Out.read())

    def testDateTimeTZName(self):
        self.runResource("builtins/dateTimeTZName.poc")
        # String tzName = TimeZone.getTimeZone("UTC").getDisplayName(Locale.ENGLISH)
        # self.assertEquals("tzName=" + tzName, Out.read())

