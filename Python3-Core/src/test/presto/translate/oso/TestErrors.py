from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestErrors(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceOSO("errors/divideByZero.poc")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceOSO("errors/indexOutOfRange-listItem.poc")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceOSO("errors/indexOutOfRange-sliceList.poc")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceOSO("errors/indexOutOfRange-sliceRange.poc")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceOSO("errors/indexOutOfRange-sliceText.poc")

    def testNullDict(self):
        self.compareResourceOSO("errors/nullDict.poc")

    def testNullItem(self):
        self.compareResourceOSO("errors/nullItem.poc")

    def testNullKey(self):
        self.compareResourceOSO("errors/nullKey.poc")

    def testNullMember(self):
        self.compareResourceOSO("errors/nullMember.poc")

    def testNullMethod(self):
        self.compareResourceOSO("errors/nullMethod.poc")

    def testUserException(self):
        self.compareResourceOSO("errors/userException.poc")


