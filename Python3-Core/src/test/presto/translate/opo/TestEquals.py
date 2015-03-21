from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestEquals(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceOPO("equals/eqBoolean.o")

    def testEqCharacter(self):
        self.compareResourceOPO("equals/eqCharacter.o")

    def testEqDate(self):
        self.compareResourceOPO("equals/eqDate.o")

    def testEqDateTime(self):
        self.compareResourceOPO("equals/eqDateTime.o")

    def testEqDecimal(self):
        self.compareResourceOPO("equals/eqDecimal.o")

    def testEqDict(self):
        self.compareResourceOPO("equals/eqDict.o")

    def testEqInteger(self):
        self.compareResourceOPO("equals/eqInteger.o")

    def testEqList(self):
        self.compareResourceOPO("equals/eqList.o")

    def testEqPeriod(self):
        self.compareResourceOPO("equals/eqPeriod.o")

    def testEqRange(self):
        self.compareResourceOPO("equals/eqRange.o")

    def testEqSet(self):
        self.compareResourceOPO("equals/eqSet.o")

    def testEqText(self):
        self.compareResourceOPO("equals/eqText.o")

    def testEqTime(self):
        self.compareResourceOPO("equals/eqTime.o")

    def testIsBoolean(self):
        self.compareResourceOPO("equals/isBoolean.o")

    def testIsInstance(self):
        self.compareResourceOPO("equals/isInstance.o")

    def testIsNotBoolean(self):
        self.compareResourceOPO("equals/isNotBoolean.o")

    def testIsNotInstance(self):
        self.compareResourceOPO("equals/isNotInstance.o")

    def testNeqBoolean(self):
        self.compareResourceOPO("equals/neqBoolean.o")

    def testNeqCharacter(self):
        self.compareResourceOPO("equals/neqCharacter.o")

    def testNeqDate(self):
        self.compareResourceOPO("equals/neqDate.o")

    def testNeqDateTime(self):
        self.compareResourceOPO("equals/neqDateTime.o")

    def testNeqDecimal(self):
        self.compareResourceOPO("equals/neqDecimal.o")

    def testNeqDict(self):
        self.compareResourceOPO("equals/neqDict.o")

    def testNeqInteger(self):
        self.compareResourceOPO("equals/neqInteger.o")

    def testNeqList(self):
        self.compareResourceOPO("equals/neqList.o")

    def testNeqPeriod(self):
        self.compareResourceOPO("equals/neqPeriod.o")

    def testNeqRange(self):
        self.compareResourceOPO("equals/neqRange.o")

    def testNeqSet(self):
        self.compareResourceOPO("equals/neqSet.o")

    def testNeqText(self):
        self.compareResourceOPO("equals/neqText.o")

    def testNeqTime(self):
        self.compareResourceOPO("equals/neqTime.o")

    def testReqText(self):
        self.compareResourceOPO("equals/reqText.o")


