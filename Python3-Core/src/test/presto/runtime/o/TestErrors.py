from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestErrors(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDivideByZero(self):
        self.checkOutput("errors/divideByZero.o")

    def testIndexOutOfRange_listItem(self):
        self.checkOutput("errors/indexOutOfRange-listItem.o")

    def testIndexOutOfRange_sliceList(self):
        self.checkOutput("errors/indexOutOfRange-sliceList.o")

    def testIndexOutOfRange_sliceRange(self):
        self.checkOutput("errors/indexOutOfRange-sliceRange.o")

    def testIndexOutOfRange_sliceText(self):
        self.checkOutput("errors/indexOutOfRange-sliceText.o")

    def testNullDict(self):
        self.checkOutput("errors/nullDict.o")

    def testNullItem(self):
        self.checkOutput("errors/nullItem.o")

    def testNullKey(self):
        self.checkOutput("errors/nullKey.o")

    def testNullMember(self):
        self.checkOutput("errors/nullMember.o")

    def testNullMethod(self):
        self.checkOutput("errors/nullMethod.o")

    def testUserException(self):
        self.checkOutput("errors/userException.o")


