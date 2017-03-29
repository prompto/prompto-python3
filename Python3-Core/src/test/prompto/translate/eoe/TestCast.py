from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDecimalCast(self):
        self.compareResourceEOE("cast/autoDecimalCast.pec")

    def testAutoDowncast(self):
        self.compareResourceEOE("cast/autoDowncast.pec")

    def testAutoIntegerCast(self):
        self.compareResourceEOE("cast/autoIntegerCast.pec")

    def testCastChild(self):
        self.compareResourceEOE("cast/castChild.pec")

    def testCastDecimal(self):
        self.compareResourceEOE("cast/castDecimal.pec")

    def testCastDocument(self):
        self.compareResourceEOE("cast/castDocument.pec")

    def testCastInteger(self):
        self.compareResourceEOE("cast/castInteger.pec")

    def testCastMissing(self):
        self.compareResourceEOE("cast/castMissing.pec")

    def testCastNull(self):
        self.compareResourceEOE("cast/castNull.pec")

    def testCastRoot(self):
        self.compareResourceEOE("cast/castRoot.pec")

    def testIsAChild(self):
        self.compareResourceEOE("cast/isAChild.pec")

    def testIsAText(self):
        self.compareResourceEOE("cast/isAText.pec")


