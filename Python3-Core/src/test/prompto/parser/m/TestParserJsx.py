from prompto.parser.Dialect import Dialect
from prompto.parser.MCleverParser import MCleverParser
from prompto.parser.m.BaseMParserTest import BaseMParserTest
from prompto.runtime.Context import Context
from prompto.utils.CodeWriter import CodeWriter


class TestParserJsx(BaseMParserTest):


    def testCanParseAndTranslateMultilineElements(self):
        jsx = "return <a>\n\t<b/>\n\t<b/>\n</a>"
        parser = MCleverParser(text=jsx)
        stmt = parser.doParse(parser.return_statement, True)
        self.assertIsNotNone(stmt.expression)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        stmt.toDialect(writer)
        out = str(writer)
        self.assertEquals(jsx, out)

    def testCanParseAndTranslateMultilineAttributes(self):
        jsx = "return <a \n\tx=\"abc\"\n\ty=\"def\"\n\tz=\"stuff\" />"
        parser = MCleverParser(text=jsx)
        stmt = parser.doParse(parser.return_statement, True)
        self.assertIsNotNone(stmt.expression)
        writer = CodeWriter(Dialect.M, Context.newGlobalContext())
        stmt.toDialect(writer)
        out = str(writer)
        self.assertEquals(jsx, out)
