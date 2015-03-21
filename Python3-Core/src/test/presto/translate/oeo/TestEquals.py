from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestEquals(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceOEO("equals/eqBoolean.o")

    def testEqCharacter(self):
        self.compareResourceOEO("equals/eqCharacter.o")

    def testEqDate(self):
        self.compareResourceOEO("equals/eqDate.o")

    def testEqDateTime(self):
        self.compareResourceOEO("equals/eqDateTime.o")

    def testEqDecimal(self):
        self.compareResourceOEO("equals/eqDecimal.o")

    def testEqDict(self):
        self.compareResourceOEO("equals/eqDict.o")

    def testEqInteger(self):
        self.compareResourceOEO("equals/eqInteger.o")

    def testEqList(self):
        self.compareResourceOEO("equals/eqList.o")

    def testEqPeriod(self):
        self.compareResourceOEO("equals/eqPeriod.o")

    def testEqRange(self):
        self.compareResourceOEO("equals/eqRange.o")

    def testEqSet(self):
        self.compareResourceOEO("equals/eqSet.o")

    def testEqText(self):
        self.compareResourceOEO("equals/eqText.o")

    def testEqTime(self):
        self.compareResourceOEO("equals/eqTime.o")

    def testIsBoolean(self):
        self.compareResourceOEO("equals/isBoolean.o")

    def testIsInstance(self):
        self.compareResourceOEO("equals/isInstance.o")

    def testIsNotBoolean(self):
        self.compareResourceOEO("equals/isNotBoolean.o")

    def testIsNotInstance(self):
        self.compareResourceOEO("equals/isNotInstance.o")

    def testNeqBoolean(self):
        self.compareResourceOEO("equals/neqBoolean.o")

    def testNeqCharacter(self):
        self.compareResourceOEO("equals/neqCharacter.o")

    def testNeqDate(self):
        self.compareResourceOEO("equals/neqDate.o")

    def testNeqDateTime(self):
        self.compareResourceOEO("equals/neqDateTime.o")

    def testNeqDecimal(self):
        self.compareResourceOEO("equals/neqDecimal.o")

    def testNeqDict(self):
        self.compareResourceOEO("equals/neqDict.o")

    def testNeqInteger(self):
        self.compareResourceOEO("equals/neqInteger.o")

    def testNeqList(self):
        self.compareResourceOEO("equals/neqList.o")

    def testNeqPeriod(self):
        self.compareResourceOEO("equals/neqPeriod.o")

    def testNeqRange(self):
        self.compareResourceOEO("equals/neqRange.o")

    def testNeqSet(self):
        self.compareResourceOEO("equals/neqSet.o")

    def testNeqText(self):
        self.compareResourceOEO("equals/neqText.o")

    def testNeqTime(self):
        self.compareResourceOEO("equals/neqTime.o")

    def testReqText(self):
        self.compareResourceOEO("equals/reqText.o")


