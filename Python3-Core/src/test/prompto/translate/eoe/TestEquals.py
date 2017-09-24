from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestEquals(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceEOE("equals/eqBoolean.pec")

    def testEqCharacter(self):
        self.compareResourceEOE("equals/eqCharacter.pec")

    def testEqDate(self):
        self.compareResourceEOE("equals/eqDate.pec")

    def testEqDateTime(self):
        self.compareResourceEOE("equals/eqDateTime.pec")

    def testEqDecimal(self):
        self.compareResourceEOE("equals/eqDecimal.pec")

    def testEqDict(self):
        self.compareResourceEOE("equals/eqDict.pec")

    def testEqInteger(self):
        self.compareResourceEOE("equals/eqInteger.pec")

    def testEqList(self):
        self.compareResourceEOE("equals/eqList.pec")

    def testEqPeriod(self):
        self.compareResourceEOE("equals/eqPeriod.pec")

    def testEqRange(self):
        self.compareResourceEOE("equals/eqRange.pec")

    def testEqSet(self):
        self.compareResourceEOE("equals/eqSet.pec")

    def testEqText(self):
        self.compareResourceEOE("equals/eqText.pec")

    def testEqTime(self):
        self.compareResourceEOE("equals/eqTime.pec")

    def testEqVersion(self):
        self.compareResourceEOE("equals/eqVersion.pec")

    def testIsBoolean(self):
        self.compareResourceEOE("equals/isBoolean.pec")

    def testIsInstance(self):
        self.compareResourceEOE("equals/isInstance.pec")

    def testIsNotBoolean(self):
        self.compareResourceEOE("equals/isNotBoolean.pec")

    def testIsNotInstance(self):
        self.compareResourceEOE("equals/isNotInstance.pec")

    def testNeqBoolean(self):
        self.compareResourceEOE("equals/neqBoolean.pec")

    def testNeqCharacter(self):
        self.compareResourceEOE("equals/neqCharacter.pec")

    def testNeqDate(self):
        self.compareResourceEOE("equals/neqDate.pec")

    def testNeqDateTime(self):
        self.compareResourceEOE("equals/neqDateTime.pec")

    def testNeqDecimal(self):
        self.compareResourceEOE("equals/neqDecimal.pec")

    def testNeqDict(self):
        self.compareResourceEOE("equals/neqDict.pec")

    def testNeqInteger(self):
        self.compareResourceEOE("equals/neqInteger.pec")

    def testNeqList(self):
        self.compareResourceEOE("equals/neqList.pec")

    def testNeqPeriod(self):
        self.compareResourceEOE("equals/neqPeriod.pec")

    def testNeqRange(self):
        self.compareResourceEOE("equals/neqRange.pec")

    def testNeqSet(self):
        self.compareResourceEOE("equals/neqSet.pec")

    def testNeqText(self):
        self.compareResourceEOE("equals/neqText.pec")

    def testNeqTime(self):
        self.compareResourceEOE("equals/neqTime.pec")

    def testReqText(self):
        self.compareResourceEOE("equals/reqText.pec")


