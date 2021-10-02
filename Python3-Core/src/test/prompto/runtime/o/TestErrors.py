from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestErrors(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDivideByZero(self):
        self.checkOutput("errors/divideByZero.poc")

    def testIndexOutOfRange_listItem(self):
        self.checkOutput("errors/indexOutOfRange-listItem.poc")

    def testIndexOutOfRange_sliceList(self):
        self.checkOutput("errors/indexOutOfRange-sliceList.poc")

    def testIndexOutOfRange_sliceRange(self):
        self.checkOutput("errors/indexOutOfRange-sliceRange.poc")

    def testIndexOutOfRange_sliceText(self):
        self.checkOutput("errors/indexOutOfRange-sliceText.poc")

    def testMemberInCatch(self):
        self.checkOutput("errors/memberInCatch.poc")

    def testNullDict(self):
        self.checkOutput("errors/nullDict.poc")

    def testNullItem(self):
        self.checkOutput("errors/nullItem.poc")

    def testNullKey(self):
        self.checkOutput("errors/nullKey.poc")

    def testNullMember(self):
        self.checkOutput("errors/nullMember.poc")

    def testNullMethod(self):
        self.checkOutput("errors/nullMethod.poc")

    def testUserException(self):
        self.checkOutput("errors/userException.poc")


