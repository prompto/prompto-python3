from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestDiv(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivDecimal(self):
        self.compareResourceOEO("div/divDecimal.o")

    def testDivInteger(self):
        self.compareResourceOEO("div/divInteger.o")

    def testIdivInteger(self):
        self.compareResourceOEO("div/idivInteger.o")

    def testModInteger(self):
        self.compareResourceOEO("div/modInteger.o")


