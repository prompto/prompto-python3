from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestBuiltins(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceOPO("builtins/dateDayOfMonth.o")

    def testDateDayOfYear(self):
        self.compareResourceOPO("builtins/dateDayOfYear.o")

    def testDateMonth(self):
        self.compareResourceOPO("builtins/dateMonth.o")

    def testDateTimeDayOfMonth(self):
        self.compareResourceOPO("builtins/dateTimeDayOfMonth.o")

    def testDateTimeDayOfYear(self):
        self.compareResourceOPO("builtins/dateTimeDayOfYear.o")

    def testDateTimeHour(self):
        self.compareResourceOPO("builtins/dateTimeHour.o")

    def testDateTimeMinute(self):
        self.compareResourceOPO("builtins/dateTimeMinute.o")

    def testDateTimeMonth(self):
        self.compareResourceOPO("builtins/dateTimeMonth.o")

    def testDateTimeSecond(self):
        self.compareResourceOPO("builtins/dateTimeSecond.o")

    def testDateTimeTZName(self):
        self.compareResourceOPO("builtins/dateTimeTZName.o")

    def testDateTimeTZOffset(self):
        self.compareResourceOPO("builtins/dateTimeTZOffset.o")

    def testDateTimeYear(self):
        self.compareResourceOPO("builtins/dateTimeYear.o")

    def testDateYear(self):
        self.compareResourceOPO("builtins/dateYear.o")

    def testDictLength(self):
        self.compareResourceOPO("builtins/dictLength.o")

    def testEnumName(self):
        self.compareResourceOPO("builtins/enumName.o")

    def testEnumSymbols(self):
        self.compareResourceOPO("builtins/enumSymbols.o")

    def testEnumValue(self):
        self.compareResourceOPO("builtins/enumValue.o")

    def testListLength(self):
        self.compareResourceOPO("builtins/listLength.o")

    def testSetLength(self):
        self.compareResourceOPO("builtins/setLength.o")

    def testTextLength(self):
        self.compareResourceOPO("builtins/textLength.o")

    def testTimeHour(self):
        self.compareResourceOPO("builtins/timeHour.o")

    def testTimeMinute(self):
        self.compareResourceOPO("builtins/timeMinute.o")

    def testTimeSecond(self):
        self.compareResourceOPO("builtins/timeSecond.o")

    def testTupleLength(self):
        self.compareResourceOPO("builtins/tupleLength.o")


