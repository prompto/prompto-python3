from prompto.parser.Dialect import Dialect
from prompto.parser.ECleverParser import ECleverParser
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.Context import Context
from prompto.utils.CodeWriter import CodeWriter


class TestParserJsx(BaseEParserTest):


    def testCanParseAndTranslateMultilineElements(self):
        jsx = "return <a>\n\t<b/>\n\t<b/>\n</a>"
        parser = ECleverParser(text=jsx)
        stmt = parser.doParse(parser.return_statement, True)
        self.assertIsNotNone(stmt.expression)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        stmt.toDialect(writer)
        out = str(writer)
        self.assertEquals(jsx, out)

    def testCanParseAndTranslateMultilineAttributes(self):
        jsx = "return <a \n\tx=\"abc\"\n\ty=\"def\"\n\tz=\"stuff\" />"
        parser = ECleverParser(text=jsx)
        stmt = parser.doParse(parser.return_statement, True)
        self.assertIsNotNone(stmt.expression)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        stmt.toDialect(writer)
        out = str(writer)
        self.assertEquals(jsx, out)
