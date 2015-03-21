from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestErrors(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceEPE("errors/divideByZero.e")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceEPE("errors/indexOutOfRange-listItem.e")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceEPE("errors/indexOutOfRange-sliceList.e")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceEPE("errors/indexOutOfRange-sliceRange.e")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceEPE("errors/indexOutOfRange-sliceText.e")

    def testNullDict(self):
        self.compareResourceEPE("errors/nullDict.e")

    def testNullItem(self):
        self.compareResourceEPE("errors/nullItem.e")

    def testNullKey(self):
        self.compareResourceEPE("errors/nullKey.e")

    def testNullMember(self):
        self.compareResourceEPE("errors/nullMember.e")

    def testNullMethod(self):
        self.compareResourceEPE("errors/nullMethod.e")

    def testUserException(self):
        self.compareResourceEPE("errors/userException.e")


