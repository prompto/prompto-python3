from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestErrors(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDivideByZero(self):
        self.checkOutput("errors/divideByZero.e")

    def testIndexOutOfRange_listItem(self):
        self.checkOutput("errors/indexOutOfRange-listItem.e")

    def testIndexOutOfRange_sliceList(self):
        self.checkOutput("errors/indexOutOfRange-sliceList.e")

    def testIndexOutOfRange_sliceRange(self):
        self.checkOutput("errors/indexOutOfRange-sliceRange.e")

    def testIndexOutOfRange_sliceText(self):
        self.checkOutput("errors/indexOutOfRange-sliceText.e")

    def testNullDict(self):
        self.checkOutput("errors/nullDict.e")

    def testNullItem(self):
        self.checkOutput("errors/nullItem.e")

    def testNullKey(self):
        self.checkOutput("errors/nullKey.e")

    def testNullMember(self):
        self.checkOutput("errors/nullMember.e")

    def testNullMethod(self):
        self.checkOutput("errors/nullMethod.e")

    def testUserException(self):
        self.checkOutput("errors/userException.e")


