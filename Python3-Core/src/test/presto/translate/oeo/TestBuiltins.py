from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestBuiltins(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceOEO("builtins/dateDayOfMonth.o")

    def testDateDayOfYear(self):
        self.compareResourceOEO("builtins/dateDayOfYear.o")

    def testDateMonth(self):
        self.compareResourceOEO("builtins/dateMonth.o")

    def testDateTimeDayOfMonth(self):
        self.compareResourceOEO("builtins/dateTimeDayOfMonth.o")

    def testDateTimeDayOfYear(self):
        self.compareResourceOEO("builtins/dateTimeDayOfYear.o")

    def testDateTimeHour(self):
        self.compareResourceOEO("builtins/dateTimeHour.o")

    def testDateTimeMinute(self):
        self.compareResourceOEO("builtins/dateTimeMinute.o")

    def testDateTimeMonth(self):
        self.compareResourceOEO("builtins/dateTimeMonth.o")

    def testDateTimeSecond(self):
        self.compareResourceOEO("builtins/dateTimeSecond.o")

    def testDateTimeTZName(self):
        self.compareResourceOEO("builtins/dateTimeTZName.o")

    def testDateTimeTZOffset(self):
        self.compareResourceOEO("builtins/dateTimeTZOffset.o")

    def testDateTimeYear(self):
        self.compareResourceOEO("builtins/dateTimeYear.o")

    def testDateYear(self):
        self.compareResourceOEO("builtins/dateYear.o")

    def testDictLength(self):
        self.compareResourceOEO("builtins/dictLength.o")

    def testEnumName(self):
        self.compareResourceOEO("builtins/enumName.o")

    def testEnumSymbols(self):
        self.compareResourceOEO("builtins/enumSymbols.o")

    def testEnumValue(self):
        self.compareResourceOEO("builtins/enumValue.o")

    def testListLength(self):
        self.compareResourceOEO("builtins/listLength.o")

    def testSetLength(self):
        self.compareResourceOEO("builtins/setLength.o")

    def testTextLength(self):
        self.compareResourceOEO("builtins/textLength.o")

    def testTimeHour(self):
        self.compareResourceOEO("builtins/timeHour.o")

    def testTimeMinute(self):
        self.compareResourceOEO("builtins/timeMinute.o")

    def testTimeSecond(self):
        self.compareResourceOEO("builtins/timeSecond.o")

    def testTupleLength(self):
        self.compareResourceOEO("builtins/tupleLength.o")


