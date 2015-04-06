from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestParserFiles ( BaseEParserTest ):

    def testEmpty(self):
        stmts = self.parseString("")
        self.assertIsNotNone(stmts)
        self.assertEquals(0,len(stmts))

    def testNative(self):
        stmts = self.parseResource("native/method.pec")
        self.assertIsNotNone(stmts)
        self.assertEquals(2,len(stmts))

    def testSpecified(self):
        stmts = self.parseResource("methods/specified.pec")
        self.assertIsNotNone(stmts)
        self.assertEquals(6,len(stmts))

    def testAttribute(self):
        stmts = self.parseResource("methods/attribute.pec")
        self.assertIsNotNone(stmts)
        self.assertEquals(6,len(stmts))

    def testImplicit(self):
        stmts = self.parseResource("methods/implicit.pec")
        self.assertIsNotNone(stmts)
        self.assertEquals(6,len(stmts))

    def testPolymorphicImplicit(self):
        stmts = self.parseResource("methods/polymorphic_implicit.pec")
        self.assertIsNotNone(stmts)
        self.assertEquals(12,len(stmts))

    def testEnumeratedCategory(self):
        stmts = self.parseResource("enums/categoryEnum.pec")
        self.assertIsNotNone(stmts)
        self.assertEquals(5,len(stmts))
