from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestErrors(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceOPO("errors/divideByZero.o")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceOPO("errors/indexOutOfRange-listItem.o")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceOPO("errors/indexOutOfRange-sliceList.o")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceOPO("errors/indexOutOfRange-sliceRange.o")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceOPO("errors/indexOutOfRange-sliceText.o")

    def testNullDict(self):
        self.compareResourceOPO("errors/nullDict.o")

    def testNullItem(self):
        self.compareResourceOPO("errors/nullItem.o")

    def testNullKey(self):
        self.compareResourceOPO("errors/nullKey.o")

    def testNullMember(self):
        self.compareResourceOPO("errors/nullMember.o")

    def testNullMethod(self):
        self.compareResourceOPO("errors/nullMethod.o")

    def testUserException(self):
        self.compareResourceOPO("errors/userException.o")


