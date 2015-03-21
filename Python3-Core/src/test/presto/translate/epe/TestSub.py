from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSub(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceEPE("sub/subDate.e")

    def testSubDateTime(self):
        self.compareResourceEPE("sub/subDateTime.e")

    def testSubDecimal(self):
        self.compareResourceEPE("sub/subDecimal.e")

    def testSubInteger(self):
        self.compareResourceEPE("sub/subInteger.e")

    def testSubPeriod(self):
        self.compareResourceEPE("sub/subPeriod.e")

    def testSubTime(self):
        self.compareResourceEPE("sub/subTime.e")


