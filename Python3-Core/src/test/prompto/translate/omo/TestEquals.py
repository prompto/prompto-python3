from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestEquals(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEqBoolean(self):
        self.compareResourceOMO("equals/eqBoolean.poc")

    def testEqCharacter(self):
        self.compareResourceOMO("equals/eqCharacter.poc")

    def testEqDate(self):
        self.compareResourceOMO("equals/eqDate.poc")

    def testEqDateTime(self):
        self.compareResourceOMO("equals/eqDateTime.poc")

    def testEqDecimal(self):
        self.compareResourceOMO("equals/eqDecimal.poc")

    def testEqDict(self):
        self.compareResourceOMO("equals/eqDict.poc")

    def testEqInteger(self):
        self.compareResourceOMO("equals/eqInteger.poc")

    def testEqList(self):
        self.compareResourceOMO("equals/eqList.poc")

    def testEqPeriod(self):
        self.compareResourceOMO("equals/eqPeriod.poc")

    def testEqRange(self):
        self.compareResourceOMO("equals/eqRange.poc")

    def testEqSet(self):
        self.compareResourceOMO("equals/eqSet.poc")

    def testEqText(self):
        self.compareResourceOMO("equals/eqText.poc")

    def testEqTime(self):
        self.compareResourceOMO("equals/eqTime.poc")

    def testEqVersion(self):
        self.compareResourceOMO("equals/eqVersion.poc")

    def testIsABoolean(self):
        self.compareResourceOMO("equals/isABoolean.poc")

    def testIsADictionary(self):
        self.compareResourceOMO("equals/isADictionary.poc")

    def testIsAParentInstance(self):
        self.compareResourceOMO("equals/isAParentInstance.poc")

    def testIsAnInstance(self):
        self.compareResourceOMO("equals/isAnInstance.poc")

    def testIsBoolean(self):
        self.compareResourceOMO("equals/isBoolean.poc")

    def testIsInstance(self):
        self.compareResourceOMO("equals/isInstance.poc")

    def testIsNotABoolean(self):
        self.compareResourceOMO("equals/isNotABoolean.poc")

    def testIsNotBoolean(self):
        self.compareResourceOMO("equals/isNotBoolean.poc")

    def testIsNotInstance(self):
        self.compareResourceOMO("equals/isNotInstance.poc")

    def testNeqBoolean(self):
        self.compareResourceOMO("equals/neqBoolean.poc")

    def testNeqCharacter(self):
        self.compareResourceOMO("equals/neqCharacter.poc")

    def testNeqDate(self):
        self.compareResourceOMO("equals/neqDate.poc")

    def testNeqDateTime(self):
        self.compareResourceOMO("equals/neqDateTime.poc")

    def testNeqDecimal(self):
        self.compareResourceOMO("equals/neqDecimal.poc")

    def testNeqDict(self):
        self.compareResourceOMO("equals/neqDict.poc")

    def testNeqInteger(self):
        self.compareResourceOMO("equals/neqInteger.poc")

    def testNeqList(self):
        self.compareResourceOMO("equals/neqList.poc")

    def testNeqPeriod(self):
        self.compareResourceOMO("equals/neqPeriod.poc")

    def testNeqRange(self):
        self.compareResourceOMO("equals/neqRange.poc")

    def testNeqSet(self):
        self.compareResourceOMO("equals/neqSet.poc")

    def testNeqText(self):
        self.compareResourceOMO("equals/neqText.poc")

    def testNeqTime(self):
        self.compareResourceOMO("equals/neqTime.poc")

    def testReqText(self):
        self.compareResourceOMO("equals/reqText.poc")


