from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestErrors(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDivideByZero(self):
        self.checkOutput("errors/divideByZero.pec")

    def testIndexOutOfRange_listItem(self):
        self.checkOutput("errors/indexOutOfRange-listItem.pec")

    def testIndexOutOfRange_sliceList(self):
        self.checkOutput("errors/indexOutOfRange-sliceList.pec")

    def testIndexOutOfRange_sliceRange(self):
        self.checkOutput("errors/indexOutOfRange-sliceRange.pec")

    def testIndexOutOfRange_sliceText(self):
        self.checkOutput("errors/indexOutOfRange-sliceText.pec")

    def testNullDict(self):
        self.checkOutput("errors/nullDict.pec")

    def testNullItem(self):
        self.checkOutput("errors/nullItem.pec")

    def testNullKey(self):
        self.checkOutput("errors/nullKey.pec")

    def testNullMember(self):
        self.checkOutput("errors/nullMember.pec")

    def testNullMethod(self):
        self.checkOutput("errors/nullMethod.pec")

    def testUserException(self):
        self.checkOutput("errors/userException.pec")


