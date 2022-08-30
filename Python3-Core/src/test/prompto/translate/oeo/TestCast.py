from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCast(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceOEO("cast/autoDowncast.poc")

    def testAutoDowncastMethod(self):
        self.compareResourceOEO("cast/autoDowncastMethod.poc")

    def testCastChild(self):
        self.compareResourceOEO("cast/castChild.poc")

    def testCastEnum(self):
        self.compareResourceOEO("cast/castEnum.poc")

    def testCastMethod(self):
        self.compareResourceOEO("cast/castMethod.poc")

    def testCastMissing(self):
        self.compareResourceOEO("cast/castMissing.poc")

    def testCastNull(self):
        self.compareResourceOEO("cast/castNull.poc")

    def testCastParent(self):
        self.compareResourceOEO("cast/castParent.poc")

    def testIsAChild(self):
        self.compareResourceOEO("cast/isAChild.poc")

    def testIsAText(self):
        self.compareResourceOEO("cast/isAText.poc")

    def testMutableEntity(self):
        self.compareResourceOEO("cast/mutableEntity.poc")

    def testMutableList(self):
        self.compareResourceOEO("cast/mutableList.poc")

    def testNullIsNotAText(self):
        self.compareResourceOEO("cast/nullIsNotAText.poc")


