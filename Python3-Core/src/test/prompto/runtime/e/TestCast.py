from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAutoDecimalCast(self):
        self.checkOutput("cast/autoDecimalCast.pec")

    def testAutoDowncast(self):
        self.checkOutput("cast/autoDowncast.pec")

    def testAutoIntegerCast(self):
        self.checkOutput("cast/autoIntegerCast.pec")

    def testCastChild(self):
        self.checkOutput("cast/castChild.pec")

    def testCastDecimal(self):
        self.checkOutput("cast/castDecimal.pec")

    def testCastDocument(self):
        self.checkOutput("cast/castDocument.pec")

    def testCastInteger(self):
        self.checkOutput("cast/castInteger.pec")

    def testCastMethod(self):
        self.checkOutput("cast/castMethod.pec")

    def testCastMissing(self):
        self.checkOutput("cast/castMissing.pec")

    def testCastNull(self):
        self.checkOutput("cast/castNull.pec")

    def testCastRoot(self):
        self.checkOutput("cast/castRoot.pec")

    def testIsAChild(self):
        self.checkOutput("cast/isAChild.pec")

    def testIsAText(self):
        self.checkOutput("cast/isAText.pec")

    def testNullisNotAText(self):
        self.checkOutput("cast/nullisNotAText.pec")


