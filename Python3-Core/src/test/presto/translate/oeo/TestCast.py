from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestCast(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceOEO("cast/autoDowncast.o")

    def testCastChild(self):
        self.compareResourceOEO("cast/castChild.o")

    def testIsAChild(self):
        self.compareResourceOEO("cast/isAChild.o")

    def testIsAText(self):
        self.compareResourceOEO("cast/isAText.o")


