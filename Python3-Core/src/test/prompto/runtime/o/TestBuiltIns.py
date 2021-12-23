from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestBuiltins(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDateDayOfMonth(self):
        self.checkOutput("builtins/dateDayOfMonth.poc")

    def testDateDayOfYear(self):
        self.checkOutput("builtins/dateDayOfYear.poc")

    def testDateMonth(self):
        self.checkOutput("builtins/dateMonth.poc")

    def testDateTimeDayOfMonth(self):
        self.checkOutput("builtins/dateTimeDayOfMonth.poc")

    def testDateTimeDayOfYear(self):
        self.checkOutput("builtins/dateTimeDayOfYear.poc")

    def testDateTimeHour(self):
        self.checkOutput("builtins/dateTimeHour.poc")

    def testDateTimeMinute(self):
        self.checkOutput("builtins/dateTimeMinute.poc")

    def testDateTimeMonth(self):
        self.checkOutput("builtins/dateTimeMonth.poc")

    def testDateTimeSecond(self):
        self.checkOutput("builtins/dateTimeSecond.poc")

    def testDateTimeYear(self):
        self.checkOutput("builtins/dateTimeYear.poc")

    def testDateYear(self):
        self.checkOutput("builtins/dateYear.poc")

    def testDictCount(self):
        self.checkOutput("builtins/dictCount.poc")

    def testDictSwap(self):
        self.checkOutput("builtins/dictSwap.poc")

    def testDocumentCount(self):
        self.checkOutput("builtins/documentCount.poc")

    def testEnumName(self):
        self.checkOutput("builtins/enumName.poc")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.poc")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.poc")

    def testIntegerFormat(self):
        self.checkOutput("builtins/integerFormat.poc")

    def testListCount(self):
        self.checkOutput("builtins/listCount.poc")

    def testListIndexOf(self):
        self.checkOutput("builtins/listIndexOf.poc")

    def testListJoin(self):
        self.checkOutput("builtins/listJoin.poc")

    def testPeriodDays(self):
        self.checkOutput("builtins/periodDays.poc")

    def testPeriodHours(self):
        self.checkOutput("builtins/periodHours.poc")

    def testPeriodMillis(self):
        self.checkOutput("builtins/periodMillis.poc")

    def testPeriodMinutes(self):
        self.checkOutput("builtins/periodMinutes.poc")

    def testPeriodMonths(self):
        self.checkOutput("builtins/periodMonths.poc")

    def testPeriodSeconds(self):
        self.checkOutput("builtins/periodSeconds.poc")

    def testPeriodWeeks(self):
        self.checkOutput("builtins/periodWeeks.poc")

    def testPeriodYears(self):
        self.checkOutput("builtins/periodYears.poc")

    def testSetCount(self):
        self.checkOutput("builtins/setCount.poc")

    def testSetJoin(self):
        self.checkOutput("builtins/setJoin.poc")

    def testTextCapitalize(self):
        self.checkOutput("builtins/textCapitalize.poc")

    def testTextCount(self):
        self.checkOutput("builtins/textCount.poc")

    def testTextIndexOf(self):
        self.checkOutput("builtins/textIndexOf.poc")

    def testTextLowercase(self):
        self.checkOutput("builtins/textLowercase.poc")

    def testTextReplace(self):
        self.checkOutput("builtins/textReplace.poc")

    def testTextReplaceAll(self):
        self.checkOutput("builtins/textReplaceAll.poc")

    def testTextSplit(self):
        self.checkOutput("builtins/textSplit.poc")

    def testTextTrim(self):
        self.checkOutput("builtins/textTrim.poc")

    def testTextUppercase(self):
        self.checkOutput("builtins/textUppercase.poc")

    def testTimeHour(self):
        self.checkOutput("builtins/timeHour.poc")

    def testTimeMinute(self):
        self.checkOutput("builtins/timeMinute.poc")

    def testTimeSecond(self):
        self.checkOutput("builtins/timeSecond.poc")

    def testTupleCount(self):
        self.checkOutput("builtins/tupleCount.poc")

    def testTupleJoin(self):
        self.checkOutput("builtins/tupleJoin.poc")


