from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCharCodePoint(self):
        self.compareResourceEME("builtins/charCodePoint.pec")

    def testDateDayOfMonth(self):
        self.compareResourceEME("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.compareResourceEME("builtins/dateDayOfYear.pec")

    def testDateMonth(self):
        self.compareResourceEME("builtins/dateMonth.pec")

    def testDateTimeDayOfMonth(self):
        self.compareResourceEME("builtins/dateTimeDayOfMonth.pec")

    def testDateTimeDayOfYear(self):
        self.compareResourceEME("builtins/dateTimeDayOfYear.pec")

    def testDateTimeHour(self):
        self.compareResourceEME("builtins/dateTimeHour.pec")

    def testDateTimeMilli(self):
        self.compareResourceEME("builtins/dateTimeMilli.pec")

    def testDateTimeMinute(self):
        self.compareResourceEME("builtins/dateTimeMinute.pec")

    def testDateTimeMonth(self):
        self.compareResourceEME("builtins/dateTimeMonth.pec")

    def testDateTimeSecond(self):
        self.compareResourceEME("builtins/dateTimeSecond.pec")

    def testDateTimeTZName(self):
        self.compareResourceEME("builtins/dateTimeTZName.pec")

    def testDateTimeTZOffset(self):
        self.compareResourceEME("builtins/dateTimeTZOffset.pec")

    def testDateTimeYear(self):
        self.compareResourceEME("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.compareResourceEME("builtins/dateYear.pec")

    def testDictCount(self):
        self.compareResourceEME("builtins/dictCount.pec")

    def testDictKeys(self):
        self.compareResourceEME("builtins/dictKeys.pec")

    def testDictValues(self):
        self.compareResourceEME("builtins/dictValues.pec")

    def testEnumName(self):
        self.compareResourceEME("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.compareResourceEME("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.compareResourceEME("builtins/enumValue.pec")

    def testListCount(self):
        self.compareResourceEME("builtins/listCount.pec")

    def testSetCount(self):
        self.compareResourceEME("builtins/setCount.pec")

    def testTextCount(self):
        self.compareResourceEME("builtins/textCount.pec")

    def testTimeHour(self):
        self.compareResourceEME("builtins/timeHour.pec")

    def testTimeMilli(self):
        self.compareResourceEME("builtins/timeMilli.pec")

    def testTimeMinute(self):
        self.compareResourceEME("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.compareResourceEME("builtins/timeSecond.pec")

    def testTupleCount(self):
        self.compareResourceEME("builtins/tupleCount.pec")


