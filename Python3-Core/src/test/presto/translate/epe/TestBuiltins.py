from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceEPE("builtins/dateDayOfMonth.e")

    def testDateDayOfYear(self):
        self.compareResourceEPE("builtins/dateDayOfYear.e")

    def testDateMonth(self):
        self.compareResourceEPE("builtins/dateMonth.e")

    def testDateTimeDayOfMonth(self):
        self.compareResourceEPE("builtins/dateTimeDayOfMonth.e")

    def testDateTimeDayOfYear(self):
        self.compareResourceEPE("builtins/dateTimeDayOfYear.e")

    def testDateTimeHour(self):
        self.compareResourceEPE("builtins/dateTimeHour.e")

    def testDateTimeMinute(self):
        self.compareResourceEPE("builtins/dateTimeMinute.e")

    def testDateTimeMonth(self):
        self.compareResourceEPE("builtins/dateTimeMonth.e")

    def testDateTimeSecond(self):
        self.compareResourceEPE("builtins/dateTimeSecond.e")

    def testDateTimeTZName(self):
        self.compareResourceEPE("builtins/dateTimeTZName.e")

    def testDateTimeTZOffset(self):
        self.compareResourceEPE("builtins/dateTimeTZOffset.e")

    def testDateTimeYear(self):
        self.compareResourceEPE("builtins/dateTimeYear.e")

    def testDateYear(self):
        self.compareResourceEPE("builtins/dateYear.e")

    def testDictLength(self):
        self.compareResourceEPE("builtins/dictLength.e")

    def testEnumName(self):
        self.compareResourceEPE("builtins/enumName.e")

    def testEnumSymbols(self):
        self.compareResourceEPE("builtins/enumSymbols.e")

    def testEnumValue(self):
        self.compareResourceEPE("builtins/enumValue.e")

    def testListLength(self):
        self.compareResourceEPE("builtins/listLength.e")

    def testSetLength(self):
        self.compareResourceEPE("builtins/setLength.e")

    def testTextLength(self):
        self.compareResourceEPE("builtins/textLength.e")

    def testTimeHour(self):
        self.compareResourceEPE("builtins/timeHour.e")

    def testTimeMinute(self):
        self.compareResourceEPE("builtins/timeMinute.e")

    def testTimeSecond(self):
        self.compareResourceEPE("builtins/timeSecond.e")

    def testTupleLength(self):
        self.compareResourceEPE("builtins/tupleLength.e")


