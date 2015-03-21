from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestEquals(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testEqBoolean(self):
        self.checkOutput("equals/eqBoolean.e")

    def testEqCharacter(self):
        self.checkOutput("equals/eqCharacter.e")

    def testEqDate(self):
        self.checkOutput("equals/eqDate.e")

    def testEqDateTime(self):
        self.checkOutput("equals/eqDateTime.e")

    def testEqDecimal(self):
        self.checkOutput("equals/eqDecimal.e")

    def testEqDict(self):
        self.checkOutput("equals/eqDict.e")

    def testEqInteger(self):
        self.checkOutput("equals/eqInteger.e")

    def testEqList(self):
        self.checkOutput("equals/eqList.e")

    def testEqPeriod(self):
        self.checkOutput("equals/eqPeriod.e")

    def testEqRange(self):
        self.checkOutput("equals/eqRange.e")

    def testEqSet(self):
        self.checkOutput("equals/eqSet.e")

    def testEqText(self):
        self.checkOutput("equals/eqText.e")

    def testEqTime(self):
        self.checkOutput("equals/eqTime.e")

    def testIsBoolean(self):
        self.checkOutput("equals/isBoolean.e")

    def testIsInstance(self):
        self.checkOutput("equals/isInstance.e")

    def testIsNotBoolean(self):
        self.checkOutput("equals/isNotBoolean.e")

    def testIsNotInstance(self):
        self.checkOutput("equals/isNotInstance.e")

    def testNeqBoolean(self):
        self.checkOutput("equals/neqBoolean.e")

    def testNeqCharacter(self):
        self.checkOutput("equals/neqCharacter.e")

    def testNeqDate(self):
        self.checkOutput("equals/neqDate.e")

    def testNeqDateTime(self):
        self.checkOutput("equals/neqDateTime.e")

    def testNeqDecimal(self):
        self.checkOutput("equals/neqDecimal.e")

    def testNeqDict(self):
        self.checkOutput("equals/neqDict.e")

    def testNeqInteger(self):
        self.checkOutput("equals/neqInteger.e")

    def testNeqList(self):
        self.checkOutput("equals/neqList.e")

    def testNeqPeriod(self):
        self.checkOutput("equals/neqPeriod.e")

    def testNeqRange(self):
        self.checkOutput("equals/neqRange.e")

    def testNeqSet(self):
        self.checkOutput("equals/neqSet.e")

    def testNeqText(self):
        self.checkOutput("equals/neqText.e")

    def testNeqTime(self):
        self.checkOutput("equals/neqTime.e")

    def testReqText(self):
        self.checkOutput("equals/reqText.e")


