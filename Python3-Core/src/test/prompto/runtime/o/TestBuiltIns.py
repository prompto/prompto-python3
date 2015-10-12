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

    def testDateTimeTZOffset(self):
        self.checkOutput("builtins/dateTimeTZOffset.poc")

    def testDateTimeYear(self):
        self.checkOutput("builtins/dateTimeYear.poc")

    def testDateYear(self):
        self.checkOutput("builtins/dateYear.poc")

    def testDictLength(self):
        self.checkOutput("builtins/dictLength.poc")

    def testEnumName(self):
        self.checkOutput("builtins/enumName.poc")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.poc")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.poc")

    def testListLength(self):
        self.checkOutput("builtins/listLength.poc")

    def testSetLength(self):
        self.checkOutput("builtins/setLength.poc")

    def testTextLength(self):
        self.checkOutput("builtins/textLength.poc")

    def testTimeHour(self):
        self.checkOutput("builtins/timeHour.poc")

    def testTimeMinute(self):
        self.checkOutput("builtins/timeMinute.poc")

    def testTimeSecond(self):
        self.checkOutput("builtins/timeSecond.poc")

    def testTupleLength(self):
        self.checkOutput("builtins/tupleLength.poc")


