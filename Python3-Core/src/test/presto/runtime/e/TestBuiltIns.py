from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestBuiltins(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDateDayOfMonth(self):
        self.checkOutput("builtins/dateDayOfMonth.e")

    def testDateDayOfYear(self):
        self.checkOutput("builtins/dateDayOfYear.e")

    def testDateMonth(self):
        self.checkOutput("builtins/dateMonth.e")

    def testDateTimeDayOfMonth(self):
        self.checkOutput("builtins/dateTimeDayOfMonth.e")

    def testDateTimeDayOfYear(self):
        self.checkOutput("builtins/dateTimeDayOfYear.e")

    def testDateTimeHour(self):
        self.checkOutput("builtins/dateTimeHour.e")

    def testDateTimeMinute(self):
        self.checkOutput("builtins/dateTimeMinute.e")

    def testDateTimeMonth(self):
        self.checkOutput("builtins/dateTimeMonth.e")

    def testDateTimeSecond(self):
        self.checkOutput("builtins/dateTimeSecond.e")

    def testDateTimeTZOffset(self):
        self.checkOutput("builtins/dateTimeTZOffset.e")

    def testDateTimeYear(self):
        self.checkOutput("builtins/dateTimeYear.e")

    def testDateYear(self):
        self.checkOutput("builtins/dateYear.e")

    def testDictLength(self):
        self.checkOutput("builtins/dictLength.e")

    def testEnumName(self):
        self.checkOutput("builtins/enumName.e")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.e")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.e")

    def testListLength(self):
        self.checkOutput("builtins/listLength.e")

    def testSetLength(self):
        self.checkOutput("builtins/setLength.e")

    def testTextLength(self):
        self.checkOutput("builtins/textLength.e")

    def testTimeHour(self):
        self.checkOutput("builtins/timeHour.e")

    def testTimeMinute(self):
        self.checkOutput("builtins/timeMinute.e")

    def testTimeSecond(self):
        self.checkOutput("builtins/timeSecond.e")

    def testTupleLength(self):
        self.checkOutput("builtins/tupleLength.e")


