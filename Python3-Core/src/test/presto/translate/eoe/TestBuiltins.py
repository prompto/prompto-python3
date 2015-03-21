from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceEOE("builtins/dateDayOfMonth.e")

    def testDateDayOfYear(self):
        self.compareResourceEOE("builtins/dateDayOfYear.e")

    def testDateMonth(self):
        self.compareResourceEOE("builtins/dateMonth.e")

    def testDateTimeDayOfMonth(self):
        self.compareResourceEOE("builtins/dateTimeDayOfMonth.e")

    def testDateTimeDayOfYear(self):
        self.compareResourceEOE("builtins/dateTimeDayOfYear.e")

    def testDateTimeHour(self):
        self.compareResourceEOE("builtins/dateTimeHour.e")

    def testDateTimeMinute(self):
        self.compareResourceEOE("builtins/dateTimeMinute.e")

    def testDateTimeMonth(self):
        self.compareResourceEOE("builtins/dateTimeMonth.e")

    def testDateTimeSecond(self):
        self.compareResourceEOE("builtins/dateTimeSecond.e")

    def testDateTimeTZName(self):
        self.compareResourceEOE("builtins/dateTimeTZName.e")

    def testDateTimeTZOffset(self):
        self.compareResourceEOE("builtins/dateTimeTZOffset.e")

    def testDateTimeYear(self):
        self.compareResourceEOE("builtins/dateTimeYear.e")

    def testDateYear(self):
        self.compareResourceEOE("builtins/dateYear.e")

    def testDictLength(self):
        self.compareResourceEOE("builtins/dictLength.e")

    def testEnumName(self):
        self.compareResourceEOE("builtins/enumName.e")

    def testEnumSymbols(self):
        self.compareResourceEOE("builtins/enumSymbols.e")

    def testEnumValue(self):
        self.compareResourceEOE("builtins/enumValue.e")

    def testListLength(self):
        self.compareResourceEOE("builtins/listLength.e")

    def testSetLength(self):
        self.compareResourceEOE("builtins/setLength.e")

    def testTextLength(self):
        self.compareResourceEOE("builtins/textLength.e")

    def testTimeHour(self):
        self.compareResourceEOE("builtins/timeHour.e")

    def testTimeMinute(self):
        self.compareResourceEOE("builtins/timeMinute.e")

    def testTimeSecond(self):
        self.compareResourceEOE("builtins/timeSecond.e")

    def testTupleLength(self):
        self.compareResourceEOE("builtins/tupleLength.e")


