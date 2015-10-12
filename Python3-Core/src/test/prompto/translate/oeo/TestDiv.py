from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestDiv(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceOEO("div/divDecimal.poc")

    def testDivInteger(self):
        self.compareResourceOEO("div/divInteger.poc")

    def testIdivInteger(self):
        self.compareResourceOEO("div/idivInteger.poc")

    def testModInteger(self):
        self.compareResourceOEO("div/modInteger.poc")


