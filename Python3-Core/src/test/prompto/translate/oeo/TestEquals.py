from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestEquals(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceOEO("equals/eqBoolean.poc")

    def testEqCharacter(self):
        self.compareResourceOEO("equals/eqCharacter.poc")

    def testEqDate(self):
        self.compareResourceOEO("equals/eqDate.poc")

    def testEqDateTime(self):
        self.compareResourceOEO("equals/eqDateTime.poc")

    def testEqDecimal(self):
        self.compareResourceOEO("equals/eqDecimal.poc")

    def testEqDict(self):
        self.compareResourceOEO("equals/eqDict.poc")

    def testEqInteger(self):
        self.compareResourceOEO("equals/eqInteger.poc")

    def testEqList(self):
        self.compareResourceOEO("equals/eqList.poc")

    def testEqPeriod(self):
        self.compareResourceOEO("equals/eqPeriod.poc")

    def testEqRange(self):
        self.compareResourceOEO("equals/eqRange.poc")

    def testEqSet(self):
        self.compareResourceOEO("equals/eqSet.poc")

    def testEqText(self):
        self.compareResourceOEO("equals/eqText.poc")

    def testEqTime(self):
        self.compareResourceOEO("equals/eqTime.poc")

    def testIsBoolean(self):
        self.compareResourceOEO("equals/isBoolean.poc")

    def testIsInstance(self):
        self.compareResourceOEO("equals/isInstance.poc")

    def testIsNotBoolean(self):
        self.compareResourceOEO("equals/isNotBoolean.poc")

    def testIsNotInstance(self):
        self.compareResourceOEO("equals/isNotInstance.poc")

    def testNeqBoolean(self):
        self.compareResourceOEO("equals/neqBoolean.poc")

    def testNeqCharacter(self):
        self.compareResourceOEO("equals/neqCharacter.poc")

    def testNeqDate(self):
        self.compareResourceOEO("equals/neqDate.poc")

    def testNeqDateTime(self):
        self.compareResourceOEO("equals/neqDateTime.poc")

    def testNeqDecimal(self):
        self.compareResourceOEO("equals/neqDecimal.poc")

    def testNeqDict(self):
        self.compareResourceOEO("equals/neqDict.poc")

    def testNeqInteger(self):
        self.compareResourceOEO("equals/neqInteger.poc")

    def testNeqList(self):
        self.compareResourceOEO("equals/neqList.poc")

    def testNeqPeriod(self):
        self.compareResourceOEO("equals/neqPeriod.poc")

    def testNeqRange(self):
        self.compareResourceOEO("equals/neqRange.poc")

    def testNeqSet(self):
        self.compareResourceOEO("equals/neqSet.poc")

    def testNeqText(self):
        self.compareResourceOEO("equals/neqText.poc")

    def testNeqTime(self):
        self.compareResourceOEO("equals/neqTime.poc")

    def testReqText(self):
        self.compareResourceOEO("equals/reqText.poc")


