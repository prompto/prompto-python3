from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDateDayOfMonth(self):
        self.compareResourceESE("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.compareResourceESE("builtins/dateDayOfYear.pec")

    def testDateMonth(self):
        self.compareResourceESE("builtins/dateMonth.pec")

    def testDateTimeDayOfMonth(self):
        self.compareResourceESE("builtins/dateTimeDayOfMonth.pec")

    def testDateTimeDayOfYear(self):
        self.compareResourceESE("builtins/dateTimeDayOfYear.pec")

    def testDateTimeHour(self):
        self.compareResourceESE("builtins/dateTimeHour.pec")

    def testDateTimeMinute(self):
        self.compareResourceESE("builtins/dateTimeMinute.pec")

    def testDateTimeMonth(self):
        self.compareResourceESE("builtins/dateTimeMonth.pec")

    def testDateTimeSecond(self):
        self.compareResourceESE("builtins/dateTimeSecond.pec")

    def testDateTimeTZName(self):
        self.compareResourceESE("builtins/dateTimeTZName.pec")

    def testDateTimeTZOffset(self):
        self.compareResourceESE("builtins/dateTimeTZOffset.pec")

    def testDateTimeYear(self):
        self.compareResourceESE("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.compareResourceESE("builtins/dateYear.pec")

    def testDictLength(self):
        self.compareResourceESE("builtins/dictLength.pec")

    def testEnumName(self):
        self.compareResourceESE("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.compareResourceESE("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.compareResourceESE("builtins/enumValue.pec")

    def testListLength(self):
        self.compareResourceESE("builtins/listLength.pec")

    def testSetLength(self):
        self.compareResourceESE("builtins/setLength.pec")

    def testTextLength(self):
        self.compareResourceESE("builtins/textLength.pec")

    def testTimeHour(self):
        self.compareResourceESE("builtins/timeHour.pec")

    def testTimeMinute(self):
        self.compareResourceESE("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.compareResourceESE("builtins/timeSecond.pec")

    def testTupleLength(self):
        self.compareResourceESE("builtins/tupleLength.pec")


