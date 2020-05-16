from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBooleanText(self):
        self.compareResourceEOE("builtins/booleanText.pec")

    def testCategoryCategory(self):
        self.compareResourceEOE("builtins/categoryCategory.pec")

    def testCategoryText(self):
        self.compareResourceEOE("builtins/categoryText.pec")

    def testCharCodePoint(self):
        self.compareResourceEOE("builtins/charCodePoint.pec")

    def testCharText(self):
        self.compareResourceEOE("builtins/charText.pec")

    def testCursorToList(self):
        self.compareResourceEOE("builtins/cursorToList.pec")

    def testDateDayOfMonth(self):
        self.compareResourceEOE("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.compareResourceEOE("builtins/dateDayOfYear.pec")

    def testDateMonth(self):
        self.compareResourceEOE("builtins/dateMonth.pec")

    def testDateText(self):
        self.compareResourceEOE("builtins/dateText.pec")

    def testDateTimeDate(self):
        self.compareResourceEOE("builtins/dateTimeDate.pec")

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

    def testDateTimeText(self):
        self.compareResourceEOE("builtins/dateTimeText.pec")

    def testDateTimeTime(self):
        self.compareResourceEOE("builtins/dateTimeTime.pec")

    def testDateTimeYear(self):
        self.compareResourceEOE("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.compareResourceEOE("builtins/dateYear.pec")

    def testDecimalText(self):
        self.compareResourceEOE("builtins/decimalText.pec")

    def testDictCount(self):
        self.compareResourceEOE("builtins/dictCount.pec")

    def testDictKeys(self):
        self.compareResourceEOE("builtins/dictKeys.pec")

    def testDictText(self):
        self.compareResourceEOE("builtins/dictText.pec")

    def testDictValues(self):
        self.compareResourceEOE("builtins/dictValues.pec")

    def testDocumentCount(self):
        self.compareResourceEOE("builtins/documentCount.pec")

    def testDocumentKeys(self):
        self.compareResourceEOE("builtins/documentKeys.pec")

    def testDocumentText(self):
        self.compareResourceEOE("builtins/documentText.pec")

    def testDocumentValues(self):
        self.compareResourceEOE("builtins/documentValues.pec")

    def testEnumName(self):
        self.compareResourceEOE("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.compareResourceEOE("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.compareResourceEOE("builtins/enumValue.pec")

    def testIntegerFormat(self):
        self.compareResourceEOE("builtins/integerFormat.pec")

    def testIntegerText(self):
        self.compareResourceEOE("builtins/integerText.pec")

    def testListCount(self):
        self.compareResourceEOE("builtins/listCount.pec")

    def testListText(self):
        self.compareResourceEOE("builtins/listText.pec")

    def testPeriodText(self):
        self.compareResourceEOE("builtins/periodText.pec")

    def testSetCount(self):
        self.compareResourceEOE("builtins/setCount.pec")

    def testSetText(self):
        self.compareResourceEOE("builtins/setText.pec")

    def testTextCapitalize(self):
        self.compareResourceEOE("builtins/textCapitalize.pec")

    def testTextCount(self):
        self.compareResourceEOE("builtins/textCount.pec")

    def testTextEndsWith(self):
        self.compareResourceEOE("builtins/textEndsWith.pec")

    def testTextLowercase(self):
        self.compareResourceEOE("builtins/textLowercase.pec")

    def testTextReplace(self):
        self.compareResourceEOE("builtins/textReplace.pec")

    def testTextReplaceAll(self):
        self.compareResourceEOE("builtins/textReplaceAll.pec")

    def testTextSplit(self):
        self.compareResourceEOE("builtins/textSplit.pec")

    def testTextStartsWith(self):
        self.compareResourceEOE("builtins/textStartsWith.pec")

    def testTextText(self):
        self.compareResourceEOE("builtins/textText.pec")

    def testTextTrim(self):
        self.compareResourceEOE("builtins/textTrim.pec")

    def testTextUppercase(self):
        self.compareResourceEOE("builtins/textUppercase.pec")

    def testTimeHour(self):
        self.compareResourceEOE("builtins/timeHour.pec")

    def testTimeMilli(self):
        self.compareResourceEOE("builtins/timeMilli.pec")

    def testTimeMinute(self):
        self.compareResourceEOE("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.compareResourceEOE("builtins/timeSecond.pec")

    def testTimeText(self):
        self.compareResourceEOE("builtins/timeText.pec")

    def testTupleCount(self):
        self.compareResourceEOE("builtins/tupleCount.pec")

    def testTupleText(self):
        self.compareResourceEOE("builtins/tupleText.pec")

    def testUuidText(self):
        self.compareResourceEOE("builtins/uuidText.pec")


