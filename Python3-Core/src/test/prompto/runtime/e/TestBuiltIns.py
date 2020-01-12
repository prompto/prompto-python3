from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testBooleanText(self):
        self.checkOutput("builtins/booleanText.pec")

    def testCategoryCategory(self):
        self.checkOutput("builtins/categoryCategory.pec")

    def testCategoryText(self):
        self.checkOutput("builtins/categoryText.pec")

    def testCharCodePoint(self):
        self.checkOutput("builtins/charCodePoint.pec")

    def testCharText(self):
        self.checkOutput("builtins/charText.pec")

    def testCursorToList(self):
        self.checkOutput("builtins/cursorToList.pec")

    def testDateDayOfMonth(self):
        self.checkOutput("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.checkOutput("builtins/dateDayOfYear.pec")

    def testDateMonth(self):
        self.checkOutput("builtins/dateMonth.pec")

    def testDateText(self):
        self.checkOutput("builtins/dateText.pec")

    def testDateTimeDate(self):
        self.checkOutput("builtins/dateTimeDate.pec")

    def testDateTimeDayOfMonth(self):
        self.checkOutput("builtins/dateTimeDayOfMonth.pec")

    def testDateTimeDayOfYear(self):
        self.checkOutput("builtins/dateTimeDayOfYear.pec")

    def testDateTimeHour(self):
        self.checkOutput("builtins/dateTimeHour.pec")

    def testDateTimeMilli(self):
        self.checkOutput("builtins/dateTimeMilli.pec")

    def testDateTimeMinute(self):
        self.checkOutput("builtins/dateTimeMinute.pec")

    def testDateTimeMonth(self):
        self.checkOutput("builtins/dateTimeMonth.pec")

    def testDateTimeSecond(self):
        self.checkOutput("builtins/dateTimeSecond.pec")

    def testDateTimeText(self):
        self.checkOutput("builtins/dateTimeText.pec")

    def testDateTimeTime(self):
        self.checkOutput("builtins/dateTimeTime.pec")

    def testDateTimeYear(self):
        self.checkOutput("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.checkOutput("builtins/dateYear.pec")

    def testDecimalText(self):
        self.checkOutput("builtins/decimalText.pec")

    def testDictCount(self):
        self.checkOutput("builtins/dictCount.pec")

    def testDictKeys(self):
        self.checkOutput("builtins/dictKeys.pec")

    def testDictText(self):
        self.checkOutput("builtins/dictText.pec")

    def testDictValues(self):
        self.checkOutput("builtins/dictValues.pec")

    def testDocumentText(self):
        self.checkOutput("builtins/documentText.pec")

    def testEnumName(self):
        self.checkOutput("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.pec")

    def testIntegerFormat(self):
        self.checkOutput("builtins/integerFormat.pec")

    def testIntegerText(self):
        self.checkOutput("builtins/integerText.pec")

    def testListCount(self):
        self.checkOutput("builtins/listCount.pec")

    def testListText(self):
        self.checkOutput("builtins/listText.pec")

    def testPeriodText(self):
        self.checkOutput("builtins/periodText.pec")

    def testSetCount(self):
        self.checkOutput("builtins/setCount.pec")

    def testSetText(self):
        self.checkOutput("builtins/setText.pec")

    def testTextCapitalize(self):
        self.checkOutput("builtins/textCapitalize.pec")

    def testTextCount(self):
        self.checkOutput("builtins/textCount.pec")

    def testTextEndsWith(self):
        self.checkOutput("builtins/textEndsWith.pec")

    def testTextLowercase(self):
        self.checkOutput("builtins/textLowercase.pec")

    def testTextReplace(self):
        self.checkOutput("builtins/textReplace.pec")

    def testTextReplaceAll(self):
        self.checkOutput("builtins/textReplaceAll.pec")

    def testTextSplit(self):
        self.checkOutput("builtins/textSplit.pec")

    def testTextStartsWith(self):
        self.checkOutput("builtins/textStartsWith.pec")

    def testTextText(self):
        self.checkOutput("builtins/textText.pec")

    def testTextTrim(self):
        self.checkOutput("builtins/textTrim.pec")

    def testTextUppercase(self):
        self.checkOutput("builtins/textUppercase.pec")

    def testTimeHour(self):
        self.checkOutput("builtins/timeHour.pec")

    def testTimeMilli(self):
        self.checkOutput("builtins/timeMilli.pec")

    def testTimeMinute(self):
        self.checkOutput("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.checkOutput("builtins/timeSecond.pec")

    def testTimeText(self):
        self.checkOutput("builtins/timeText.pec")

    def testTupleCount(self):
        self.checkOutput("builtins/tupleCount.pec")

    def testTupleText(self):
        self.checkOutput("builtins/tupleText.pec")

    def testUuidText(self):
        self.checkOutput("builtins/uuidText.pec")


