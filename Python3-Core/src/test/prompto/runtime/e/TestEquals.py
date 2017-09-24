from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestEquals(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testEqBoolean(self):
        self.checkOutput("equals/eqBoolean.pec")

    def testEqCharacter(self):
        self.checkOutput("equals/eqCharacter.pec")

    def testEqDate(self):
        self.checkOutput("equals/eqDate.pec")

    def testEqDateTime(self):
        self.checkOutput("equals/eqDateTime.pec")

    def testEqDecimal(self):
        self.checkOutput("equals/eqDecimal.pec")

    def testEqDict(self):
        self.checkOutput("equals/eqDict.pec")

    def testEqInteger(self):
        self.checkOutput("equals/eqInteger.pec")

    def testEqList(self):
        self.checkOutput("equals/eqList.pec")

    def testEqPeriod(self):
        self.checkOutput("equals/eqPeriod.pec")

    def testEqRange(self):
        self.checkOutput("equals/eqRange.pec")

    def testEqSet(self):
        self.checkOutput("equals/eqSet.pec")

    def testEqText(self):
        self.checkOutput("equals/eqText.pec")

    def testEqTime(self):
        self.checkOutput("equals/eqTime.pec")

    def testEqVersion(self):
        self.checkOutput("equals/eqVersion.pec")

    def testIsBoolean(self):
        self.checkOutput("equals/isBoolean.pec")

    def testIsInstance(self):
        self.checkOutput("equals/isInstance.pec")

    def testIsNotBoolean(self):
        self.checkOutput("equals/isNotBoolean.pec")

    def testIsNotInstance(self):
        self.checkOutput("equals/isNotInstance.pec")

    def testNeqBoolean(self):
        self.checkOutput("equals/neqBoolean.pec")

    def testNeqCharacter(self):
        self.checkOutput("equals/neqCharacter.pec")

    def testNeqDate(self):
        self.checkOutput("equals/neqDate.pec")

    def testNeqDateTime(self):
        self.checkOutput("equals/neqDateTime.pec")

    def testNeqDecimal(self):
        self.checkOutput("equals/neqDecimal.pec")

    def testNeqDict(self):
        self.checkOutput("equals/neqDict.pec")

    def testNeqInteger(self):
        self.checkOutput("equals/neqInteger.pec")

    def testNeqList(self):
        self.checkOutput("equals/neqList.pec")

    def testNeqPeriod(self):
        self.checkOutput("equals/neqPeriod.pec")

    def testNeqRange(self):
        self.checkOutput("equals/neqRange.pec")

    def testNeqSet(self):
        self.checkOutput("equals/neqSet.pec")

    def testNeqText(self):
        self.checkOutput("equals/neqText.pec")

    def testNeqTime(self):
        self.checkOutput("equals/neqTime.pec")

    def testReqText(self):
        self.checkOutput("equals/reqText.pec")


