from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestEquals(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceOSO("equals/eqBoolean.poc")

    def testEqCharacter(self):
        self.compareResourceOSO("equals/eqCharacter.poc")

    def testEqDate(self):
        self.compareResourceOSO("equals/eqDate.poc")

    def testEqDateTime(self):
        self.compareResourceOSO("equals/eqDateTime.poc")

    def testEqDecimal(self):
        self.compareResourceOSO("equals/eqDecimal.poc")

    def testEqDict(self):
        self.compareResourceOSO("equals/eqDict.poc")

    def testEqInteger(self):
        self.compareResourceOSO("equals/eqInteger.poc")

    def testEqList(self):
        self.compareResourceOSO("equals/eqList.poc")

    def testEqPeriod(self):
        self.compareResourceOSO("equals/eqPeriod.poc")

    def testEqRange(self):
        self.compareResourceOSO("equals/eqRange.poc")

    def testEqSet(self):
        self.compareResourceOSO("equals/eqSet.poc")

    def testEqText(self):
        self.compareResourceOSO("equals/eqText.poc")

    def testEqTime(self):
        self.compareResourceOSO("equals/eqTime.poc")

    def testIsBoolean(self):
        self.compareResourceOSO("equals/isBoolean.poc")

    def testIsInstance(self):
        self.compareResourceOSO("equals/isInstance.poc")

    def testIsNotBoolean(self):
        self.compareResourceOSO("equals/isNotBoolean.poc")

    def testIsNotInstance(self):
        self.compareResourceOSO("equals/isNotInstance.poc")

    def testNeqBoolean(self):
        self.compareResourceOSO("equals/neqBoolean.poc")

    def testNeqCharacter(self):
        self.compareResourceOSO("equals/neqCharacter.poc")

    def testNeqDate(self):
        self.compareResourceOSO("equals/neqDate.poc")

    def testNeqDateTime(self):
        self.compareResourceOSO("equals/neqDateTime.poc")

    def testNeqDecimal(self):
        self.compareResourceOSO("equals/neqDecimal.poc")

    def testNeqDict(self):
        self.compareResourceOSO("equals/neqDict.poc")

    def testNeqInteger(self):
        self.compareResourceOSO("equals/neqInteger.poc")

    def testNeqList(self):
        self.compareResourceOSO("equals/neqList.poc")

    def testNeqPeriod(self):
        self.compareResourceOSO("equals/neqPeriod.poc")

    def testNeqRange(self):
        self.compareResourceOSO("equals/neqRange.poc")

    def testNeqSet(self):
        self.compareResourceOSO("equals/neqSet.poc")

    def testNeqText(self):
        self.compareResourceOSO("equals/neqText.poc")

    def testNeqTime(self):
        self.compareResourceOSO("equals/neqTime.poc")

    def testReqText(self):
        self.compareResourceOSO("equals/reqText.poc")


