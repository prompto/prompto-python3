from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testBooleanJson(self):
        self.checkOutput("builtins/booleanJson.pec")

    def testBooleanText(self):
        self.checkOutput("builtins/booleanText.pec")

    def testCategoryCategory(self):
        self.checkOutput("builtins/categoryCategory.pec")

    def testCategoryJson(self):
        self.checkOutput("builtins/categoryJson.pec")

    def testCategoryText(self):
        self.checkOutput("builtins/categoryText.pec")

    def testCharCodePoint(self):
        self.checkOutput("builtins/charCodePoint.pec")

    def testCharJson(self):
        self.checkOutput("builtins/charJson.pec")

    def testCharText(self):
        self.checkOutput("builtins/charText.pec")

    def testCursorToList(self):
        self.checkOutput("builtins/cursorToList.pec")

    def testDateDayOfMonth(self):
        self.checkOutput("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.checkOutput("builtins/dateDayOfYear.pec")

    def testDateJson(self):
        self.checkOutput("builtins/dateJson.pec")

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

    def testDateTimeJson(self):
        self.checkOutput("builtins/dateTimeJson.pec")

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

    def testDecimalJson(self):
        self.checkOutput("builtins/decimalJson.pec")

    def testDecimalText(self):
        self.checkOutput("builtins/decimalText.pec")

    def testDictCount(self):
        self.checkOutput("builtins/dictCount.pec")

    def testDictJson(self):
        self.checkOutput("builtins/dictJson.pec")

    def testDictKeys(self):
        self.checkOutput("builtins/dictKeys.pec")

    def testDictText(self):
        self.checkOutput("builtins/dictText.pec")

    def testDictValues(self):
        self.checkOutput("builtins/dictValues.pec")

    def testDocumentCount(self):
        self.checkOutput("builtins/documentCount.pec")

    def testDocumentJson(self):
        self.checkOutput("builtins/documentJson.pec")

    def testDocumentKeys(self):
        self.checkOutput("builtins/documentKeys.pec")

    def testDocumentText(self):
        self.checkOutput("builtins/documentText.pec")

    def testDocumentValues(self):
        self.checkOutput("builtins/documentValues.pec")

    def testEnumName(self):
        self.checkOutput("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.pec")

    def testIntegerFormat(self):
        self.checkOutput("builtins/integerFormat.pec")

    def testIntegerJson(self):
        self.checkOutput("builtins/integerJson.pec")

    def testIntegerText(self):
        self.checkOutput("builtins/integerText.pec")

    def testIteratorToList(self):
        self.checkOutput("builtins/iteratorToList.pec")

    def testIteratorToSet(self):
        self.checkOutput("builtins/iteratorToSet.pec")

    def testListCount(self):
        self.checkOutput("builtins/listCount.pec")

    def testListJson(self):
        self.checkOutput("builtins/listJson.pec")

    def testListText(self):
        self.checkOutput("builtins/listText.pec")

    def testListToSet(self):
        self.checkOutput("builtins/listToSet.pec")

    def testPeriodDays(self):
        self.checkOutput("builtins/periodDays.pec")

    def testPeriodHours(self):
        self.checkOutput("builtins/periodHours.pec")

    def testPeriodJson(self):
        self.checkOutput("builtins/periodJson.pec")

    def testPeriodMillis(self):
        self.checkOutput("builtins/periodMillis.pec")

    def testPeriodMinutes(self):
        self.checkOutput("builtins/periodMinutes.pec")

    def testPeriodMonths(self):
        self.checkOutput("builtins/periodMonths.pec")

    def testPeriodSeconds(self):
        self.checkOutput("builtins/periodSeconds.pec")

    def testPeriodText(self):
        self.checkOutput("builtins/periodText.pec")

    def testPeriodWeeks(self):
        self.checkOutput("builtins/periodWeeks.pec")

    def testPeriodYears(self):
        self.checkOutput("builtins/periodYears.pec")

    def testSetCount(self):
        self.checkOutput("builtins/setCount.pec")

    def testSetJson(self):
        self.checkOutput("builtins/setJson.pec")

    def testSetText(self):
        self.checkOutput("builtins/setText.pec")

    def testSetToList(self):
        self.checkOutput("builtins/setToList.pec")

    def testTextCapitalize(self):
        self.checkOutput("builtins/textCapitalize.pec")

    def testTextCount(self):
        self.checkOutput("builtins/textCount.pec")

    def testTextEndsWith(self):
        self.checkOutput("builtins/textEndsWith.pec")

    def testTextJson(self):
        self.checkOutput("builtins/textJson.pec")

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

    def testTimeJson(self):
        self.checkOutput("builtins/timeJson.pec")

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

    def testUuidJson(self):
        self.checkOutput("builtins/uuidJson.pec")

    def testUuidText(self):
        self.checkOutput("builtins/uuidText.pec")

    def testVersionMembers(self):
        self.checkOutput("builtins/versionMembers.pec")


