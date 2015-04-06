from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestDiv(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceEOE("div/divDecimal.pec")

    def testDivInteger(self):
        self.compareResourceEOE("div/divInteger.pec")

    def testIdivInteger(self):
        self.compareResourceEOE("div/idivInteger.pec")

    def testModInteger(self):
        self.compareResourceEOE("div/modInteger.pec")


