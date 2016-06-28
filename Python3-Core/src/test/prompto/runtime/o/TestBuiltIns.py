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

    def testEnumName(self):
        self.checkOutput("builtins/enumName.poc")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.poc")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.poc")

    def testListCount(self):
        self.checkOutput("builtins/listCount.poc")

    def testSetCount(self):
        self.checkOutput("builtins/setCount.poc")

    def testTextCount(self):
        self.checkOutput("builtins/textCount.poc")

    def testTimeHour(self):
        self.checkOutput("builtins/timeHour.poc")

    def testTimeMinute(self):
        self.checkOutput("builtins/timeMinute.poc")

    def testTimeSecond(self):
        self.checkOutput("builtins/timeSecond.poc")

    def testTupleCount(self):
        self.checkOutput("builtins/tupleCount.poc")


