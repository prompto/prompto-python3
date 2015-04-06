from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestCast(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceOSO("cast/autoDowncast.poc")

    def testCastChild(self):
        self.compareResourceOSO("cast/castChild.poc")

    def testIsAChild(self):
        self.compareResourceOSO("cast/isAChild.poc")

    def testIsAText(self):
        self.compareResourceOSO("cast/isAText.poc")


