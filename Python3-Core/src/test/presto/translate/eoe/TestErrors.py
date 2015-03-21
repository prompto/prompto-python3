from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestErrors(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceEOE("errors/divideByZero.e")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceEOE("errors/indexOutOfRange-listItem.e")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceEOE("errors/indexOutOfRange-sliceList.e")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceEOE("errors/indexOutOfRange-sliceRange.e")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceEOE("errors/indexOutOfRange-sliceText.e")

    def testNullDict(self):
        self.compareResourceEOE("errors/nullDict.e")

    def testNullItem(self):
        self.compareResourceEOE("errors/nullItem.e")

    def testNullKey(self):
        self.compareResourceEOE("errors/nullKey.e")

    def testNullMember(self):
        self.compareResourceEOE("errors/nullMember.e")

    def testNullMethod(self):
        self.compareResourceEOE("errors/nullMethod.e")

    def testUserException(self):
        self.compareResourceEOE("errors/userException.e")


