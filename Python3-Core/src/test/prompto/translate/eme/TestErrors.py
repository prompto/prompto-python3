from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestErrors(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceEME("errors/divideByZero.pec")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceEME("errors/indexOutOfRange-listItem.pec")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceEME("errors/indexOutOfRange-sliceList.pec")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceEME("errors/indexOutOfRange-sliceRange.pec")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceEME("errors/indexOutOfRange-sliceText.pec")

    def testNullDict(self):
        self.compareResourceEME("errors/nullDict.pec")

    def testNullItem(self):
        self.compareResourceEME("errors/nullItem.pec")

    def testNullKey(self):
        self.compareResourceEME("errors/nullKey.pec")

    def testNullMember(self):
        self.compareResourceEME("errors/nullMember.pec")

    def testNullMethod(self):
        self.compareResourceEME("errors/nullMethod.pec")

    def testUnexpected(self):
        self.compareResourceEME("errors/unexpected.pec")

    def testUserException(self):
        self.compareResourceEME("errors/userException.pec")


