from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestEquals(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceESE("equals/eqBoolean.pec")

    def testEqCharacter(self):
        self.compareResourceESE("equals/eqCharacter.pec")

    def testEqDate(self):
        self.compareResourceESE("equals/eqDate.pec")

    def testEqDateTime(self):
        self.compareResourceESE("equals/eqDateTime.pec")

    def testEqDecimal(self):
        self.compareResourceESE("equals/eqDecimal.pec")

    def testEqDict(self):
        self.compareResourceESE("equals/eqDict.pec")

    def testEqInteger(self):
        self.compareResourceESE("equals/eqInteger.pec")

    def testEqList(self):
        self.compareResourceESE("equals/eqList.pec")

    def testEqPeriod(self):
        self.compareResourceESE("equals/eqPeriod.pec")

    def testEqRange(self):
        self.compareResourceESE("equals/eqRange.pec")

    def testEqSet(self):
        self.compareResourceESE("equals/eqSet.pec")

    def testEqText(self):
        self.compareResourceESE("equals/eqText.pec")

    def testEqTime(self):
        self.compareResourceESE("equals/eqTime.pec")

    def testIsBoolean(self):
        self.compareResourceESE("equals/isBoolean.pec")

    def testIsInstance(self):
        self.compareResourceESE("equals/isInstance.pec")

    def testIsNotBoolean(self):
        self.compareResourceESE("equals/isNotBoolean.pec")

    def testIsNotInstance(self):
        self.compareResourceESE("equals/isNotInstance.pec")

    def testNeqBoolean(self):
        self.compareResourceESE("equals/neqBoolean.pec")

    def testNeqCharacter(self):
        self.compareResourceESE("equals/neqCharacter.pec")

    def testNeqDate(self):
        self.compareResourceESE("equals/neqDate.pec")

    def testNeqDateTime(self):
        self.compareResourceESE("equals/neqDateTime.pec")

    def testNeqDecimal(self):
        self.compareResourceESE("equals/neqDecimal.pec")

    def testNeqDict(self):
        self.compareResourceESE("equals/neqDict.pec")

    def testNeqInteger(self):
        self.compareResourceESE("equals/neqInteger.pec")

    def testNeqList(self):
        self.compareResourceESE("equals/neqList.pec")

    def testNeqPeriod(self):
        self.compareResourceESE("equals/neqPeriod.pec")

    def testNeqRange(self):
        self.compareResourceESE("equals/neqRange.pec")

    def testNeqSet(self):
        self.compareResourceESE("equals/neqSet.pec")

    def testNeqText(self):
        self.compareResourceESE("equals/neqText.pec")

    def testNeqTime(self):
        self.compareResourceESE("equals/neqTime.pec")

    def testReqText(self):
        self.compareResourceESE("equals/reqText.pec")


