from antlr4 import ParseTreeWalker
from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.parser.ECleverParser import ECleverParser
from presto.parser.EPrestoBuilder import EPrestoBuilder
from presto.runtime.utils.Out import Out
from presto.runtime.Context import Context
from presto.grammar.CategoryArgument import CategoryArgument
from presto.type.TextType import TextType
from presto.literal.TextLiteral import TextLiteral
import sys

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
        builder = EPrestoBuilder(parser)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        statement = builder.getNodeValue(tree)
        context = Context.newGlobalContext()
        arg = CategoryArgument(TextType.instance, "value")
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

