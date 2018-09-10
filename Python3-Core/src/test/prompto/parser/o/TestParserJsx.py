from prompto.parser.Dialect import Dialect
from prompto.parser.OCleverParser import OCleverParser
from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.Context import Context
from prompto.utils.CodeWriter import CodeWriter


class TestParserJsx(BaseOParserTest):


    def testCanParseAndTranslateMultilineElements(self):
        jsx = "return <a>\n\t<b/>\n\t<b/>\n</a>;"
        parser = OCleverParser(text=jsx)
        stmt = parser.doParse(parser.return_statement)
        self.assertIsNotNone(stmt.expression)
        writer = CodeWriter(Dialect.E, Context.newGlobalContext())
        stmt.toDialect(writer)
        writer.append(";")
        out = str(writer)
        self.assertEquals(jsx, out)

    def testCanParseAndTranslateMultilineAttributes(self):
        jsx = "return <a \n\tx=\"abc\"\n\ty=\"def\"\n\tz=\"stuff\" />;"
        parser = OCleverParser(text=jsx)
        stmt = parser.doParse(parser.return_statement)
        self.assertIsNotNone(stmt.expression)
        writer = CodeWriter(Dialect.M, Context.newGlobalContext())
        stmt.toDialect(writer)
        writer.append(";")
        out = str(writer)
        self.assertEquals(jsx, out)
