from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestParserFiles ( BaseEParserTest ):

    def testEmpty(self):
        stmts = self.parseString("")
        self.assertIsNotNone(stmts)
        self.assertEqual(0,len(stmts))

    def testNative(self):
        stmts = self.parseResource("native/method.pec")
        self.assertIsNotNone(stmts)
        self.assertEqual(2,len(stmts))

    def testSpecified(self):
        stmts = self.parseResource("methods/specified.pec")
        self.assertIsNotNone(stmts)
        self.assertEqual(6,len(stmts))

    def testAttribute(self):
        stmts = self.parseResource("methods/attribute.pec")
        self.assertIsNotNone(stmts)
        self.assertEqual(6,len(stmts))

    def testEnumeratedCategory(self):
        stmts = self.parseResource("enums/categoryEnum.pec")
        self.assertIsNotNone(stmts)
        self.assertEqual(7,len(stmts))
