from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAutoDowncast(self):
        self.compareResourceESE("cast/autoDowncast.pec")

    def testCastChild(self):
        self.compareResourceESE("cast/castChild.pec")

    def testCastMissing(self):
        self.compareResourceESE("cast/castMissing.pec")

    def testCastNull(self):
        self.compareResourceESE("cast/castNull.pec")

    def testIsAChild(self):
        self.compareResourceESE("cast/isAChild.pec")

    def testIsAText(self):
        self.compareResourceESE("cast/isAText.pec")


