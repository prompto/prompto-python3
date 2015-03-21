from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestBuiltins(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDateDayOfMonth(self):
        self.checkOutput("builtins/dateDayOfMonth.o")

    def testDateDayOfYear(self):
        self.checkOutput("builtins/dateDayOfYear.o")

    def testDateMonth(self):
        self.checkOutput("builtins/dateMonth.o")

    def testDateTimeDayOfMonth(self):
        self.checkOutput("builtins/dateTimeDayOfMonth.o")

    def testDateTimeDayOfYear(self):
        self.checkOutput("builtins/dateTimeDayOfYear.o")

    def testDateTimeHour(self):
        self.checkOutput("builtins/dateTimeHour.o")

    def testDateTimeMinute(self):
        self.checkOutput("builtins/dateTimeMinute.o")

    def testDateTimeMonth(self):
        self.checkOutput("builtins/dateTimeMonth.o")

    def testDateTimeSecond(self):
        self.checkOutput("builtins/dateTimeSecond.o")

    def testDateTimeTZOffset(self):
        self.checkOutput("builtins/dateTimeTZOffset.o")

    def testDateTimeYear(self):
        self.checkOutput("builtins/dateTimeYear.o")

    def testDateYear(self):
        self.checkOutput("builtins/dateYear.o")

    def testDictLength(self):
        self.checkOutput("builtins/dictLength.o")

    def testEnumName(self):
        self.checkOutput("builtins/enumName.o")

    def testEnumSymbols(self):
        self.checkOutput("builtins/enumSymbols.o")

    def testEnumValue(self):
        self.checkOutput("builtins/enumValue.o")

    def testListLength(self):
        self.checkOutput("builtins/listLength.o")

    def testSetLength(self):
        self.checkOutput("builtins/setLength.o")

    def testTextLength(self):
        self.checkOutput("builtins/textLength.o")

    def testTimeHour(self):
        self.checkOutput("builtins/timeHour.o")

    def testTimeMinute(self):
        self.checkOutput("builtins/timeMinute.o")

    def testTimeSecond(self):
        self.checkOutput("builtins/timeSecond.o")

    def testTupleLength(self):
        self.checkOutput("builtins/tupleLength.o")


