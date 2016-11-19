from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestDiv(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceOMO("div/divDecimal.poc")

    def testDivInteger(self):
        self.compareResourceOMO("div/divInteger.poc")

    def testIdivInteger(self):
        self.compareResourceOMO("div/idivInteger.poc")

    def testModInteger(self):
        self.compareResourceOMO("div/modInteger.poc")


