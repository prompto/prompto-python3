from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestErrors(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceESE("errors/divideByZero.pec")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceESE("errors/indexOutOfRange-listItem.pec")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceESE("errors/indexOutOfRange-sliceList.pec")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceESE("errors/indexOutOfRange-sliceRange.pec")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceESE("errors/indexOutOfRange-sliceText.pec")

    def testNullDict(self):
        self.compareResourceESE("errors/nullDict.pec")

    def testNullItem(self):
        self.compareResourceESE("errors/nullItem.pec")

    def testNullKey(self):
        self.compareResourceESE("errors/nullKey.pec")

    def testNullMember(self):
        self.compareResourceESE("errors/nullMember.pec")

    def testNullMethod(self):
        self.compareResourceESE("errors/nullMethod.pec")

    def testUserException(self):
        self.compareResourceESE("errors/userException.pec")


