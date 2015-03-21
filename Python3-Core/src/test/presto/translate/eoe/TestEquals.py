from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestEquals(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceEOE("equals/eqBoolean.e")

    def testEqCharacter(self):
        self.compareResourceEOE("equals/eqCharacter.e")

    def testEqDate(self):
        self.compareResourceEOE("equals/eqDate.e")

    def testEqDateTime(self):
        self.compareResourceEOE("equals/eqDateTime.e")

    def testEqDecimal(self):
        self.compareResourceEOE("equals/eqDecimal.e")

    def testEqDict(self):
        self.compareResourceEOE("equals/eqDict.e")

    def testEqInteger(self):
        self.compareResourceEOE("equals/eqInteger.e")

    def testEqList(self):
        self.compareResourceEOE("equals/eqList.e")

    def testEqPeriod(self):
        self.compareResourceEOE("equals/eqPeriod.e")

    def testEqRange(self):
        self.compareResourceEOE("equals/eqRange.e")

    def testEqSet(self):
        self.compareResourceEOE("equals/eqSet.e")

    def testEqText(self):
        self.compareResourceEOE("equals/eqText.e")

    def testEqTime(self):
        self.compareResourceEOE("equals/eqTime.e")

    def testIsBoolean(self):
        self.compareResourceEOE("equals/isBoolean.e")

    def testIsInstance(self):
        self.compareResourceEOE("equals/isInstance.e")

    def testIsNotBoolean(self):
        self.compareResourceEOE("equals/isNotBoolean.e")

    def testIsNotInstance(self):
        self.compareResourceEOE("equals/isNotInstance.e")

    def testNeqBoolean(self):
        self.compareResourceEOE("equals/neqBoolean.e")

    def testNeqCharacter(self):
        self.compareResourceEOE("equals/neqCharacter.e")

    def testNeqDate(self):
        self.compareResourceEOE("equals/neqDate.e")

    def testNeqDateTime(self):
        self.compareResourceEOE("equals/neqDateTime.e")

    def testNeqDecimal(self):
        self.compareResourceEOE("equals/neqDecimal.e")

    def testNeqDict(self):
        self.compareResourceEOE("equals/neqDict.e")

    def testNeqInteger(self):
        self.compareResourceEOE("equals/neqInteger.e")

    def testNeqList(self):
        self.compareResourceEOE("equals/neqList.e")

    def testNeqPeriod(self):
        self.compareResourceEOE("equals/neqPeriod.e")

    def testNeqRange(self):
        self.compareResourceEOE("equals/neqRange.e")

    def testNeqSet(self):
        self.compareResourceEOE("equals/neqSet.e")

    def testNeqText(self):
        self.compareResourceEOE("equals/neqText.e")

    def testNeqTime(self):
        self.compareResourceEOE("equals/neqTime.e")

    def testReqText(self):
        self.compareResourceEOE("equals/reqText.e")


