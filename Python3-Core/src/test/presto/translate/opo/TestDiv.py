from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestDiv(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceOPO("div/divDecimal.o")

    def testDivInteger(self):
        self.compareResourceOPO("div/divInteger.o")

    def testIdivInteger(self):
        self.compareResourceOPO("div/idivInteger.o")

    def testModInteger(self):
        self.compareResourceOPO("div/modInteger.o")


