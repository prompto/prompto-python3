from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestDiv(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceEOE("div/divDecimal.e")

    def testDivInteger(self):
        self.compareResourceEOE("div/divInteger.e")

    def testIdivInteger(self):
        self.compareResourceEOE("div/idivInteger.e")

    def testModInteger(self):
        self.compareResourceEOE("div/modInteger.e")


