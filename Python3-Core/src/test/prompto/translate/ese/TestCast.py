from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDecimalCast(self):
        self.compareResourceESE("cast/autoDecimalCast.pec")

    def testAutoDowncast(self):
        self.compareResourceESE("cast/autoDowncast.pec")

    def testAutoIntegerCast(self):
        self.compareResourceESE("cast/autoIntegerCast.pec")

    def testCastChild(self):
        self.compareResourceESE("cast/castChild.pec")

    def testCastDecimal(self):
        self.compareResourceESE("cast/castDecimal.pec")

    def testCastInteger(self):
        self.compareResourceESE("cast/castInteger.pec")

    def testCastMissing(self):
        self.compareResourceESE("cast/castMissing.pec")

    def testCastNull(self):
        self.compareResourceESE("cast/castNull.pec")

    def testIsAChild(self):
        self.compareResourceESE("cast/isAChild.pec")

    def testIsAText(self):
        self.compareResourceESE("cast/isAText.pec")


