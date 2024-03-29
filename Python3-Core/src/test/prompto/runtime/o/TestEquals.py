from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestEquals(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testEqBoolean(self):
        self.checkOutput("equals/eqBoolean.poc")

    def testEqCharacter(self):
        self.checkOutput("equals/eqCharacter.poc")

    def testEqDate(self):
        self.checkOutput("equals/eqDate.poc")

    def testEqDateTime(self):
        self.checkOutput("equals/eqDateTime.poc")

    def testEqDecimal(self):
        self.checkOutput("equals/eqDecimal.poc")

    def testEqDict(self):
        self.checkOutput("equals/eqDict.poc")

    def testEqInteger(self):
        self.checkOutput("equals/eqInteger.poc")

    def testEqList(self):
        self.checkOutput("equals/eqList.poc")

    def testEqPeriod(self):
        self.checkOutput("equals/eqPeriod.poc")

    def testEqRange(self):
        self.checkOutput("equals/eqRange.poc")

    def testEqSet(self):
        self.checkOutput("equals/eqSet.poc")

    def testEqText(self):
        self.checkOutput("equals/eqText.poc")

    def testEqTime(self):
        self.checkOutput("equals/eqTime.poc")

    def testEqVersion(self):
        self.checkOutput("equals/eqVersion.poc")

    def testIsABoolean(self):
        self.checkOutput("equals/isABoolean.poc")

    def testIsADictionary(self):
        self.checkOutput("equals/isADictionary.poc")

    def testIsAParentInstance(self):
        self.checkOutput("equals/isAParentInstance.poc")

    def testIsAnInstance(self):
        self.checkOutput("equals/isAnInstance.poc")

    def testIsAnInstanceTernary(self):
        self.checkOutput("equals/isAnInstanceTernary.poc")

    def testIsBoolean(self):
        self.checkOutput("equals/isBoolean.poc")

    def testIsInstance(self):
        self.checkOutput("equals/isInstance.poc")

    def testIsNotABoolean(self):
        self.checkOutput("equals/isNotABoolean.poc")

    def testIsNotBoolean(self):
        self.checkOutput("equals/isNotBoolean.poc")

    def testIsNotInstance(self):
        self.checkOutput("equals/isNotInstance.poc")

    def testNeqBoolean(self):
        self.checkOutput("equals/neqBoolean.poc")

    def testNeqCharacter(self):
        self.checkOutput("equals/neqCharacter.poc")

    def testNeqDate(self):
        self.checkOutput("equals/neqDate.poc")

    def testNeqDateTime(self):
        self.checkOutput("equals/neqDateTime.poc")

    def testNeqDecimal(self):
        self.checkOutput("equals/neqDecimal.poc")

    def testNeqDict(self):
        self.checkOutput("equals/neqDict.poc")

    def testNeqInteger(self):
        self.checkOutput("equals/neqInteger.poc")

    def testNeqList(self):
        self.checkOutput("equals/neqList.poc")

    def testNeqPeriod(self):
        self.checkOutput("equals/neqPeriod.poc")

    def testNeqRange(self):
        self.checkOutput("equals/neqRange.poc")

    def testNeqSet(self):
        self.checkOutput("equals/neqSet.poc")

    def testNeqText(self):
        self.checkOutput("equals/neqText.poc")

    def testNeqTime(self):
        self.checkOutput("equals/neqTime.poc")

    def testReqText(self):
        self.checkOutput("equals/reqText.poc")


