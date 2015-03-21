from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestDiv(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceEPE("div/divDecimal.e")

    def testDivInteger(self):
        self.compareResourceEPE("div/divInteger.e")

    def testIdivInteger(self):
        self.compareResourceEPE("div/idivInteger.e")

    def testModInteger(self):
        self.compareResourceEPE("div/modInteger.e")


