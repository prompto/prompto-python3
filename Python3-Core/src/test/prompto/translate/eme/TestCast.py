from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDecimalCast(self):
        self.compareResourceEME("cast/autoDecimalCast.pec")

    def testAutoDowncast(self):
        self.compareResourceEME("cast/autoDowncast.pec")

    def testAutoIntegerCast(self):
        self.compareResourceEME("cast/autoIntegerCast.pec")

    def testCastChild(self):
        self.compareResourceEME("cast/castChild.pec")

    def testCastDecimal(self):
        self.compareResourceEME("cast/castDecimal.pec")

    def testCastDocument(self):
        self.compareResourceEME("cast/castDocument.pec")

    def testCastInteger(self):
        self.compareResourceEME("cast/castInteger.pec")

    def testCastMethod(self):
        self.compareResourceEME("cast/castMethod.pec")

    def testCastMissing(self):
        self.compareResourceEME("cast/castMissing.pec")

    def testCastNull(self):
        self.compareResourceEME("cast/castNull.pec")

    def testCastRoot(self):
        self.compareResourceEME("cast/castRoot.pec")

    def testIsAChild(self):
        self.compareResourceEME("cast/isAChild.pec")

    def testIsAText(self):
        self.compareResourceEME("cast/isAText.pec")

    def testNullisNotAText(self):
        self.compareResourceEME("cast/nullisNotAText.pec")


