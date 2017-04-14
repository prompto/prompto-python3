from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestBuiltins(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceOEO("builtins/dateDayOfMonth.poc")

    def testDateDayOfYear(self):
        self.compareResourceOEO("builtins/dateDayOfYear.poc")

    def testDateMonth(self):
        self.compareResourceOEO("builtins/dateMonth.poc")

    def testDateTimeDayOfMonth(self):
        self.compareResourceOEO("builtins/dateTimeDayOfMonth.poc")

    def testDateTimeDayOfYear(self):
        self.compareResourceOEO("builtins/dateTimeDayOfYear.poc")

    def testDateTimeHour(self):
        self.compareResourceOEO("builtins/dateTimeHour.poc")

    def testDateTimeMinute(self):
        self.compareResourceOEO("builtins/dateTimeMinute.poc")

    def testDateTimeMonth(self):
        self.compareResourceOEO("builtins/dateTimeMonth.poc")

    def testDateTimeSecond(self):
        self.compareResourceOEO("builtins/dateTimeSecond.poc")

    def testDateTimeTZName(self):
        self.compareResourceOEO("builtins/dateTimeTZName.poc")

    def testDateTimeTZOffset(self):
        self.compareResourceOEO("builtins/dateTimeTZOffset.poc")

    def testDateTimeYear(self):
        self.compareResourceOEO("builtins/dateTimeYear.poc")

    def testDateYear(self):
        self.compareResourceOEO("builtins/dateYear.poc")

    def testDictCount(self):
        self.compareResourceOEO("builtins/dictCount.poc")

    def testEnumName(self):
        self.compareResourceOEO("builtins/enumName.poc")

    def testEnumSymbols(self):
        self.compareResourceOEO("builtins/enumSymbols.poc")

    def testEnumValue(self):
        self.compareResourceOEO("builtins/enumValue.poc")

    def testIntegerFormat(self):
        self.compareResourceOEO("builtins/integerFormat.poc")

    def testListCount(self):
        self.compareResourceOEO("builtins/listCount.poc")

    def testSetCount(self):
        self.compareResourceOEO("builtins/setCount.poc")

    def testTextCapitalize(self):
        self.compareResourceOEO("builtins/textCapitalize.poc")

    def testTextCount(self):
        self.compareResourceOEO("builtins/textCount.poc")

    def testTextLowercase(self):
        self.compareResourceOEO("builtins/textLowercase.poc")

    def testTextReplace(self):
        self.compareResourceOEO("builtins/textReplace.poc")

    def testTextSplit(self):
        self.compareResourceOEO("builtins/textSplit.poc")

    def testTextTrim(self):
        self.compareResourceOEO("builtins/textTrim.poc")

    def testTextUppercase(self):
        self.compareResourceOEO("builtins/textUppercase.poc")

    def testTimeHour(self):
        self.compareResourceOEO("builtins/timeHour.poc")

    def testTimeMinute(self):
        self.compareResourceOEO("builtins/timeMinute.poc")

    def testTimeSecond(self):
        self.compareResourceOEO("builtins/timeSecond.poc")

    def testTupleCount(self):
        self.compareResourceOEO("builtins/tupleCount.poc")


