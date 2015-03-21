from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestCast(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceOPO("cast/autoDowncast.o")

    def testCastChild(self):
        self.compareResourceOPO("cast/castChild.o")

    def testIsAChild(self):
        self.compareResourceOPO("cast/isAChild.o")

    def testIsAText(self):
        self.compareResourceOPO("cast/isAText.o")


