from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceEOE("cast/autoDowncast.e")

    def testCastChild(self):
        self.compareResourceEOE("cast/castChild.e")

    def testIsAChild(self):
        self.compareResourceEOE("cast/isAChild.e")

    def testIsAText(self):
        self.compareResourceEOE("cast/isAText.e")


