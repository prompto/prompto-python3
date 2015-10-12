from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestErrors(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceEOE("errors/divideByZero.pec")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceEOE("errors/indexOutOfRange-listItem.pec")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceEOE("errors/indexOutOfRange-sliceList.pec")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceEOE("errors/indexOutOfRange-sliceRange.pec")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceEOE("errors/indexOutOfRange-sliceText.pec")

    def testNullDict(self):
        self.compareResourceEOE("errors/nullDict.pec")

    def testNullItem(self):
        self.compareResourceEOE("errors/nullItem.pec")

    def testNullKey(self):
        self.compareResourceEOE("errors/nullKey.pec")

    def testNullMember(self):
        self.compareResourceEOE("errors/nullMember.pec")

    def testNullMethod(self):
        self.compareResourceEOE("errors/nullMethod.pec")

    def testUnexpected(self):
        self.compareResourceEOE("errors/unexpected.pec")

    def testUserException(self):
        self.compareResourceEOE("errors/userException.pec")


