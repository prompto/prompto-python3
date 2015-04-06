from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestCast(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceOEO("cast/autoDowncast.poc")

    def testCastChild(self):
        self.compareResourceOEO("cast/castChild.poc")

    def testIsAChild(self):
        self.compareResourceOEO("cast/isAChild.poc")

    def testIsAText(self):
        self.compareResourceOEO("cast/isAText.poc")


