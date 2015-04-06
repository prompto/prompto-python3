from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestBuiltins(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceOSO("builtins/dateDayOfMonth.poc")

    def testDateDayOfYear(self):
        self.compareResourceOSO("builtins/dateDayOfYear.poc")

    def testDateMonth(self):
        self.compareResourceOSO("builtins/dateMonth.poc")

    def testDateTimeDayOfMonth(self):
        self.compareResourceOSO("builtins/dateTimeDayOfMonth.poc")

    def testDateTimeDayOfYear(self):
        self.compareResourceOSO("builtins/dateTimeDayOfYear.poc")

    def testDateTimeHour(self):
        self.compareResourceOSO("builtins/dateTimeHour.poc")

    def testDateTimeMinute(self):
        self.compareResourceOSO("builtins/dateTimeMinute.poc")

    def testDateTimeMonth(self):
        self.compareResourceOSO("builtins/dateTimeMonth.poc")

    def testDateTimeSecond(self):
        self.compareResourceOSO("builtins/dateTimeSecond.poc")

    def testDateTimeTZName(self):
        self.compareResourceOSO("builtins/dateTimeTZName.poc")

    def testDateTimeTZOffset(self):
        self.compareResourceOSO("builtins/dateTimeTZOffset.poc")

    def testDateTimeYear(self):
        self.compareResourceOSO("builtins/dateTimeYear.poc")

    def testDateYear(self):
        self.compareResourceOSO("builtins/dateYear.poc")

    def testDictLength(self):
        self.compareResourceOSO("builtins/dictLength.poc")

    def testEnumName(self):
        self.compareResourceOSO("builtins/enumName.poc")

    def testEnumSymbols(self):
        self.compareResourceOSO("builtins/enumSymbols.poc")

    def testEnumValue(self):
        self.compareResourceOSO("builtins/enumValue.poc")

    def testListLength(self):
        self.compareResourceOSO("builtins/listLength.poc")

    def testSetLength(self):
        self.compareResourceOSO("builtins/setLength.poc")

    def testTextLength(self):
        self.compareResourceOSO("builtins/textLength.poc")

    def testTimeHour(self):
        self.compareResourceOSO("builtins/timeHour.poc")

    def testTimeMinute(self):
        self.compareResourceOSO("builtins/timeMinute.poc")

    def testTimeSecond(self):
        self.compareResourceOSO("builtins/timeSecond.poc")

    def testTupleLength(self):
        self.compareResourceOSO("builtins/tupleLength.poc")


