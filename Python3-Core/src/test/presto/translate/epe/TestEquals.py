from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestEquals(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceEPE("equals/eqBoolean.e")

    def testEqCharacter(self):
        self.compareResourceEPE("equals/eqCharacter.e")

    def testEqDate(self):
        self.compareResourceEPE("equals/eqDate.e")

    def testEqDateTime(self):
        self.compareResourceEPE("equals/eqDateTime.e")

    def testEqDecimal(self):
        self.compareResourceEPE("equals/eqDecimal.e")

    def testEqDict(self):
        self.compareResourceEPE("equals/eqDict.e")

    def testEqInteger(self):
        self.compareResourceEPE("equals/eqInteger.e")

    def testEqList(self):
        self.compareResourceEPE("equals/eqList.e")

    def testEqPeriod(self):
        self.compareResourceEPE("equals/eqPeriod.e")

    def testEqRange(self):
        self.compareResourceEPE("equals/eqRange.e")

    def testEqSet(self):
        self.compareResourceEPE("equals/eqSet.e")

    def testEqText(self):
        self.compareResourceEPE("equals/eqText.e")

    def testEqTime(self):
        self.compareResourceEPE("equals/eqTime.e")

    def testIsBoolean(self):
        self.compareResourceEPE("equals/isBoolean.e")

    def testIsInstance(self):
        self.compareResourceEPE("equals/isInstance.e")

    def testIsNotBoolean(self):
        self.compareResourceEPE("equals/isNotBoolean.e")

    def testIsNotInstance(self):
        self.compareResourceEPE("equals/isNotInstance.e")

    def testNeqBoolean(self):
        self.compareResourceEPE("equals/neqBoolean.e")

    def testNeqCharacter(self):
        self.compareResourceEPE("equals/neqCharacter.e")

    def testNeqDate(self):
        self.compareResourceEPE("equals/neqDate.e")

    def testNeqDateTime(self):
        self.compareResourceEPE("equals/neqDateTime.e")

    def testNeqDecimal(self):
        self.compareResourceEPE("equals/neqDecimal.e")

    def testNeqDict(self):
        self.compareResourceEPE("equals/neqDict.e")

    def testNeqInteger(self):
        self.compareResourceEPE("equals/neqInteger.e")

    def testNeqList(self):
        self.compareResourceEPE("equals/neqList.e")

    def testNeqPeriod(self):
        self.compareResourceEPE("equals/neqPeriod.e")

    def testNeqRange(self):
        self.compareResourceEPE("equals/neqRange.e")

    def testNeqSet(self):
        self.compareResourceEPE("equals/neqSet.e")

    def testNeqText(self):
        self.compareResourceEPE("equals/neqText.e")

    def testNeqTime(self):
        self.compareResourceEPE("equals/neqTime.e")

    def testReqText(self):
        self.compareResourceEPE("equals/reqText.e")


