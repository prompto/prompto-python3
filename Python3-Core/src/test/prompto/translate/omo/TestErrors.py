from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestErrors(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDivideByZero(self):
        self.compareResourceOMO("errors/divideByZero.poc")

    def testIndexOutOfRange_listItem(self):
        self.compareResourceOMO("errors/indexOutOfRange-listItem.poc")

    def testIndexOutOfRange_sliceList(self):
        self.compareResourceOMO("errors/indexOutOfRange-sliceList.poc")

    def testIndexOutOfRange_sliceRange(self):
        self.compareResourceOMO("errors/indexOutOfRange-sliceRange.poc")

    def testIndexOutOfRange_sliceText(self):
        self.compareResourceOMO("errors/indexOutOfRange-sliceText.poc")

    def testNullDict(self):
        self.compareResourceOMO("errors/nullDict.poc")

    def testNullItem(self):
        self.compareResourceOMO("errors/nullItem.poc")

    def testNullKey(self):
        self.compareResourceOMO("errors/nullKey.poc")

    def testNullMember(self):
        self.compareResourceOMO("errors/nullMember.poc")

    def testNullMethod(self):
        self.compareResourceOMO("errors/nullMethod.poc")

    def testUserException(self):
        self.compareResourceOMO("errors/userException.poc")


