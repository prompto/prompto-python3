from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBooleanText(self):
        self.compareResourceEME("builtins/booleanText.pec")

    def testCategoryText(self):
        self.compareResourceEME("builtins/categoryText.pec")

    def testCharCodePoint(self):
        self.compareResourceEME("builtins/charCodePoint.pec")

    def testCharText(self):
        self.compareResourceEME("builtins/charText.pec")

    def testDateDayOfMonth(self):
        self.compareResourceEME("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.compareResourceEME("builtins/dateDayOfYear.pec")

    def testDateMonth(self):
        self.compareResourceEME("builtins/dateMonth.pec")

    def testDateText(self):
        self.compareResourceEME("builtins/dateText.pec")

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

    def testDateTimeText(self):
        self.compareResourceEME("builtins/dateTimeText.pec")

    def testDateTimeYear(self):
        self.compareResourceEME("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.compareResourceEME("builtins/dateYear.pec")

    def testDecimalText(self):
        self.compareResourceEME("builtins/decimalText.pec")

    def testDictCount(self):
        self.compareResourceEME("builtins/dictCount.pec")

    def testDictKeys(self):
        self.compareResourceEME("builtins/dictKeys.pec")

    def testDictText(self):
        self.compareResourceEME("builtins/dictText.pec")

    def testDictValues(self):
        self.compareResourceEME("builtins/dictValues.pec")

    def testDocumentText(self):
        self.compareResourceEME("builtins/documentText.pec")

    def testEnumName(self):
        self.compareResourceEME("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.compareResourceEME("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.compareResourceEME("builtins/enumValue.pec")

    def testIntegerFormat(self):
        self.compareResourceEME("builtins/integerFormat.pec")

    def testIntegerText(self):
        self.compareResourceEME("builtins/integerText.pec")

    def testListCount(self):
        self.compareResourceEME("builtins/listCount.pec")

    def testListText(self):
        self.compareResourceEME("builtins/listText.pec")

    def testPeriodText(self):
        self.compareResourceEME("builtins/periodText.pec")

    def testSetCount(self):
        self.compareResourceEME("builtins/setCount.pec")

    def testSetText(self):
        self.compareResourceEME("builtins/setText.pec")

    def testTextCapitalize(self):
        self.compareResourceEME("builtins/textCapitalize.pec")

    def testTextCount(self):
        self.compareResourceEME("builtins/textCount.pec")

    def testTextEndsWith(self):
        self.compareResourceEME("builtins/textEndsWith.pec")

    def testTextLowercase(self):
        self.compareResourceEME("builtins/textLowercase.pec")

    def testTextReplace(self):
        self.compareResourceEME("builtins/textReplace.pec")

    def testTextReplaceAll(self):
        self.compareResourceEME("builtins/textReplaceAll.pec")

    def testTextSplit(self):
        self.compareResourceEME("builtins/textSplit.pec")

    def testTextStartsWith(self):
        self.compareResourceEME("builtins/textStartsWith.pec")

    def testTextText(self):
        self.compareResourceEME("builtins/textText.pec")

    def testTextTrim(self):
        self.compareResourceEME("builtins/textTrim.pec")

    def testTextUppercase(self):
        self.compareResourceEME("builtins/textUppercase.pec")

    def testTimeHour(self):
        self.compareResourceEME("builtins/timeHour.pec")

    def testTimeMilli(self):
        self.compareResourceEME("builtins/timeMilli.pec")

    def testTimeMinute(self):
        self.compareResourceEME("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.compareResourceEME("builtins/timeSecond.pec")

    def testTimeText(self):
        self.compareResourceEME("builtins/timeText.pec")

    def testTupleCount(self):
        self.compareResourceEME("builtins/tupleCount.pec")

    def testTupleText(self):
        self.compareResourceEME("builtins/tupleText.pec")

    def testUuidText(self):
        self.compareResourceEME("builtins/uuidText.pec")


