from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSub(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceEOE("sub/subDate.e")

    def testSubDateTime(self):
        self.compareResourceEOE("sub/subDateTime.e")

    def testSubDecimal(self):
        self.compareResourceEOE("sub/subDecimal.e")

    def testSubInteger(self):
        self.compareResourceEOE("sub/subInteger.e")

    def testSubPeriod(self):
        self.compareResourceEOE("sub/subPeriod.e")

    def testSubTime(self):
        self.compareResourceEOE("sub/subTime.e")


