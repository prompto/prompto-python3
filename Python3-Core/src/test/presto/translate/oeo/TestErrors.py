from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestErrors(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceOEO("errors/divideByZero.poc")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceOEO("errors/indexOutOfRange-listItem.poc")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceOEO("errors/indexOutOfRange-sliceList.poc")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceOEO("errors/indexOutOfRange-sliceRange.poc")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceOEO("errors/indexOutOfRange-sliceText.poc")

    def testNullDict(self):
        self.compareResourceOEO("errors/nullDict.poc")

    def testNullItem(self):
        self.compareResourceOEO("errors/nullItem.poc")

    def testNullKey(self):
        self.compareResourceOEO("errors/nullKey.poc")

    def testNullMember(self):
        self.compareResourceOEO("errors/nullMember.poc")

    def testNullMethod(self):
        self.compareResourceOEO("errors/nullMethod.poc")

    def testUserException(self):
        self.compareResourceOEO("errors/userException.poc")


