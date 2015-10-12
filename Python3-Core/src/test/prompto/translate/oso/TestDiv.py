from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestDiv(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceOSO("div/divDecimal.poc")

    def testDivInteger(self):
        self.compareResourceOSO("div/divInteger.poc")

    def testIdivInteger(self):
        self.compareResourceOSO("div/idivInteger.poc")

    def testModInteger(self):
        self.compareResourceOSO("div/modInteger.poc")


