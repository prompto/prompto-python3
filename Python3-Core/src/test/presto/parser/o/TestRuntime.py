from antlr4 import ParseTreeWalker
from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.parser.OPrestoBuilder import OPrestoBuilder
from presto.runtime.utils.Out import Out
from presto.parser.OCleverParser import OCleverParser
from presto.runtime.Context import Context
from presto.grammar.CategoryArgument import CategoryArgument
from presto.type.TextType import TextType
from presto.literal.TextLiteral import TextLiteral
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
        builder = OPrestoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        statement = builder.getNodeValue(tree)
        context = Context.newGlobalContext()
        arg = CategoryArgument(TextType.instance, "value")
        arg.register(context)
        context.setValue("value", TextLiteral("\"test\"")) # StringLiteral trims enclosing quotes
        result = statement.interpret(context, None)
        self.assertIsNone(result)
        self.assertEquals("test", Out.read())

    def testReturnText(self):
        self.runResource("native/return.o")
        self.assertEquals(sys.platform, Out.read())

    def testDateTimeTZName(self):
        self.runResource("builtins/dateTimeTZName.o")
        # String tzName = TimeZone.getTimeZone("UTC").getDisplayName(Locale.ENGLISH)
        # self.assertEquals("tzName=" + tzName, Out.read())

