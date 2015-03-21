from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceEPE("cast/autoDowncast.e")

    def testCastChild(self):
        self.compareResourceEPE("cast/castChild.e")

    def testIsAChild(self):
        self.compareResourceEPE("cast/isAChild.e")

    def testIsAText(self):
        self.compareResourceEPE("cast/isAText.e")


