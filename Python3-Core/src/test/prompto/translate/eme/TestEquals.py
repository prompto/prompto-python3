from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestEquals(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceEME("equals/eqBoolean.pec")

    def testEqCharacter(self):
        self.compareResourceEME("equals/eqCharacter.pec")

    def testEqDate(self):
        self.compareResourceEME("equals/eqDate.pec")

    def testEqDateTime(self):
        self.compareResourceEME("equals/eqDateTime.pec")

    def testEqDecimal(self):
        self.compareResourceEME("equals/eqDecimal.pec")

    def testEqDict(self):
        self.compareResourceEME("equals/eqDict.pec")

    def testEqInteger(self):
        self.compareResourceEME("equals/eqInteger.pec")

    def testEqList(self):
        self.compareResourceEME("equals/eqList.pec")

    def testEqPeriod(self):
        self.compareResourceEME("equals/eqPeriod.pec")

    def testEqRange(self):
        self.compareResourceEME("equals/eqRange.pec")

    def testEqSet(self):
        self.compareResourceEME("equals/eqSet.pec")

    def testEqText(self):
        self.compareResourceEME("equals/eqText.pec")

    def testEqTime(self):
        self.compareResourceEME("equals/eqTime.pec")

    def testIsBoolean(self):
        self.compareResourceEME("equals/isBoolean.pec")

    def testIsInstance(self):
        self.compareResourceEME("equals/isInstance.pec")

    def testIsNotBoolean(self):
        self.compareResourceEME("equals/isNotBoolean.pec")

    def testIsNotInstance(self):
        self.compareResourceEME("equals/isNotInstance.pec")

    def testNeqBoolean(self):
        self.compareResourceEME("equals/neqBoolean.pec")

    def testNeqCharacter(self):
        self.compareResourceEME("equals/neqCharacter.pec")

    def testNeqDate(self):
        self.compareResourceEME("equals/neqDate.pec")

    def testNeqDateTime(self):
        self.compareResourceEME("equals/neqDateTime.pec")

    def testNeqDecimal(self):
        self.compareResourceEME("equals/neqDecimal.pec")

    def testNeqDict(self):
        self.compareResourceEME("equals/neqDict.pec")

    def testNeqInteger(self):
        self.compareResourceEME("equals/neqInteger.pec")

    def testNeqList(self):
        self.compareResourceEME("equals/neqList.pec")

    def testNeqPeriod(self):
        self.compareResourceEME("equals/neqPeriod.pec")

    def testNeqRange(self):
        self.compareResourceEME("equals/neqRange.pec")

    def testNeqSet(self):
        self.compareResourceEME("equals/neqSet.pec")

    def testNeqText(self):
        self.compareResourceEME("equals/neqText.pec")

    def testNeqTime(self):
        self.compareResourceEME("equals/neqTime.pec")

    def testReqText(self):
        self.compareResourceEME("equals/reqText.pec")


