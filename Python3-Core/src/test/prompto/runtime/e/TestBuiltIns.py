from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDateDayOfMonth(self):
        self.checkOutput("builtins/dateDayOfMonth.pec")

    def testDateDayOfYear(self):
        self.checkOutput("builtins/dateDayOfYear.pec")

    def testDateMonth(self):
        self.checkOutput("builtins/dateMonth.pec")

    def testDateTimeDayOfMonth(self):
        self.checkOutput("builtins/dateTimeDayOfMonth.pec")

    def testDateTimeDayOfYear(self):
        self.checkOutput("builtins/dateTimeDayOfYear.pec")

    def testDateTimeHour(self):
        self.checkOutput("builtins/dateTimeHour.pec")

    def testDateTimeMinute(self):
        self.checkOutput("builtins/dateTimeMinute.pec")

    def testDateTimeMonth(self):
        self.checkOutput("builtins/dateTimeMonth.pec")

    def testDateTimeSecond(self):
        self.checkOutput("builtins/dateTimeSecond.pec")

    def testDateTimeTZOffset(self):
        self.checkOutput("builtins/dateTimeTZOffset.pec")

    def testDateTimeYear(self):
        self.checkOutput("builtins/dateTimeYear.pec")

    def testDateYear(self):
        self.checkOutput("builtins/dateYear.pec")

    def testDictLength(self):
        self.checkOutput("builtins/dictLength.pec")

    def testEnumName(self):
        self.checkOutput("builtins/enumName.pec")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.pec")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.pec")

    def testListLength(self):
        self.checkOutput("builtins/listLength.pec")

    def testSetLength(self):
        self.checkOutput("builtins/setLength.pec")

    def testTextLength(self):
        self.checkOutput("builtins/textLength.pec")

    def testTimeHour(self):
        self.checkOutput("builtins/timeHour.pec")

    def testTimeMinute(self):
        self.checkOutput("builtins/timeMinute.pec")

    def testTimeSecond(self):
        self.checkOutput("builtins/timeSecond.pec")

    def testTupleLength(self):
        self.checkOutput("builtins/tupleLength.pec")


