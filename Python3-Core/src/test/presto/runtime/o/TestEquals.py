from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestEquals(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testEqBoolean(self):
        self.checkOutput("equals/eqBoolean.o")

    def testEqCharacter(self):
        self.checkOutput("equals/eqCharacter.o")

    def testEqDate(self):
        self.checkOutput("equals/eqDate.o")

    def testEqDateTime(self):
        self.checkOutput("equals/eqDateTime.o")

    def testEqDecimal(self):
        self.checkOutput("equals/eqDecimal.o")

    def testEqDict(self):
        self.checkOutput("equals/eqDict.o")

    def testEqInteger(self):
        self.checkOutput("equals/eqInteger.o")

    def testEqList(self):
        self.checkOutput("equals/eqList.o")

    def testEqPeriod(self):
        self.checkOutput("equals/eqPeriod.o")

    def testEqRange(self):
        self.checkOutput("equals/eqRange.o")

    def testEqSet(self):
        self.checkOutput("equals/eqSet.o")

    def testEqText(self):
        self.checkOutput("equals/eqText.o")

    def testEqTime(self):
        self.checkOutput("equals/eqTime.o")

    def testIsBoolean(self):
        self.checkOutput("equals/isBoolean.o")

    def testIsInstance(self):
        self.checkOutput("equals/isInstance.o")

    def testIsNotBoolean(self):
        self.checkOutput("equals/isNotBoolean.o")

    def testIsNotInstance(self):
        self.checkOutput("equals/isNotInstance.o")

    def testNeqBoolean(self):
        self.checkOutput("equals/neqBoolean.o")

    def testNeqCharacter(self):
        self.checkOutput("equals/neqCharacter.o")

    def testNeqDate(self):
        self.checkOutput("equals/neqDate.o")

    def testNeqDateTime(self):
        self.checkOutput("equals/neqDateTime.o")

    def testNeqDecimal(self):
        self.checkOutput("equals/neqDecimal.o")

    def testNeqDict(self):
        self.checkOutput("equals/neqDict.o")

    def testNeqInteger(self):
        self.checkOutput("equals/neqInteger.o")

    def testNeqList(self):
        self.checkOutput("equals/neqList.o")

    def testNeqPeriod(self):
        self.checkOutput("equals/neqPeriod.o")

    def testNeqRange(self):
        self.checkOutput("equals/neqRange.o")

    def testNeqSet(self):
        self.checkOutput("equals/neqSet.o")

    def testNeqText(self):
        self.checkOutput("equals/neqText.o")

    def testNeqTime(self):
        self.checkOutput("equals/neqTime.o")

    def testReqText(self):
        self.checkOutput("equals/reqText.o")


