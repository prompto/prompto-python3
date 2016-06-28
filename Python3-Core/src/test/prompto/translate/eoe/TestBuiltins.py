from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCharCodePoint(self):
        self.compareResourceEOE("builtins/charCodePoint.pec")

    def testDateDayOfMonth(self):
        self.compareResourceEOE("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.compareResourceEOE("builtins/dateDayOfYear.pec")

    def testDateMonth(self):
        self.compareResourceEOE("builtins/dateMonth.pec")

    def testDateTimeDayOfMonth(self):
        self.compareResourceEOE("builtins/dateTimeDayOfMonth.pec")

    def testDateTimeDayOfYear(self):
        self.compareResourceEOE("builtins/dateTimeDayOfYear.pec")

    def testDateTimeHour(self):
        self.compareResourceEOE("builtins/dateTimeHour.pec")

    def testDateTimeMilli(self):
        self.compareResourceEOE("builtins/dateTimeMilli.pec")

    def testDateTimeMinute(self):
        self.compareResourceEOE("builtins/dateTimeMinute.pec")

    def testDateTimeMonth(self):
        self.compareResourceEOE("builtins/dateTimeMonth.pec")

    def testDateTimeSecond(self):
        self.compareResourceEOE("builtins/dateTimeSecond.pec")

    def testDateTimeTZName(self):
        self.compareResourceEOE("builtins/dateTimeTZName.pec")

    def testDateTimeTZOffset(self):
        self.compareResourceEOE("builtins/dateTimeTZOffset.pec")

    def testDateTimeYear(self):
        self.compareResourceEOE("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.compareResourceEOE("builtins/dateYear.pec")

    def testDictCount(self):
        self.compareResourceEOE("builtins/dictCount.pec")

    def testDictKeys(self):
        self.compareResourceEOE("builtins/dictKeys.pec")

    def testDictValues(self):
        self.compareResourceEOE("builtins/dictValues.pec")

    def testEnumName(self):
        self.compareResourceEOE("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.compareResourceEOE("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.compareResourceEOE("builtins/enumValue.pec")

    def testListCount(self):
        self.compareResourceEOE("builtins/listCount.pec")

    def testSetCount(self):
        self.compareResourceEOE("builtins/setCount.pec")

    def testTextCount(self):
        self.compareResourceEOE("builtins/textCount.pec")

    def testTimeHour(self):
        self.compareResourceEOE("builtins/timeHour.pec")

    def testTimeMilli(self):
        self.compareResourceEOE("builtins/timeMilli.pec")

    def testTimeMinute(self):
        self.compareResourceEOE("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.compareResourceEOE("builtins/timeSecond.pec")

    def testTupleCount(self):
        self.compareResourceEOE("builtins/tupleCount.pec")


