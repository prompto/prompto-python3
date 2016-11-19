from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDiv(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceEME("div/divDecimal.pec")

    def testDivInteger(self):
        self.compareResourceEME("div/divInteger.pec")

    def testIdivInteger(self):
        self.compareResourceEME("div/idivInteger.pec")

    def testModInteger(self):
        self.compareResourceEME("div/modInteger.pec")


