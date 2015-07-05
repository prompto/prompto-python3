from prompto.parser.o.BaseOParserTest import BaseOParserTest


class TestParserFiles(BaseOParserTest):

    def testEmpty(self):
        stmts = self.parseString("")
        self.assertIsNotNone(stmts)
        self.assertEquals(0, len(stmts))
