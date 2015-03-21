from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestErrors(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceOEO("errors/divideByZero.o")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceOEO("errors/indexOutOfRange-listItem.o")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceOEO("errors/indexOutOfRange-sliceList.o")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceOEO("errors/indexOutOfRange-sliceRange.o")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceOEO("errors/indexOutOfRange-sliceText.o")

    def testNullDict(self):
        self.compareResourceOEO("errors/nullDict.o")

    def testNullItem(self):
        self.compareResourceOEO("errors/nullItem.o")

    def testNullKey(self):
        self.compareResourceOEO("errors/nullKey.o")

    def testNullMember(self):
        self.compareResourceOEO("errors/nullMember.o")

    def testNullMethod(self):
        self.compareResourceOEO("errors/nullMethod.o")

    def testUserException(self):
        self.compareResourceOEO("errors/userException.o")


