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

    def testCastMethod(self):
        self.compareResourceOEO("cast/castMethod.poc")

    def testCastMissing(self):
        self.compareResourceOEO("cast/castMissing.poc")

    def testCastNull(self):
        self.compareResourceOEO("cast/castNull.poc")

    def testIsAChild(self):
        self.compareResourceOEO("cast/isAChild.poc")

    def testIsAText(self):
        self.compareResourceOEO("cast/isAText.poc")

    def testNullIsNotAText(self):
        self.compareResourceOEO("cast/nullIsNotAText.poc")


