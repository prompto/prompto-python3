from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestFetch(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFetchFromList(self):
        self.compareResourceESE("fetch/fetchFromList.pec")

    def testFetchFromSet(self):
        self.compareResourceESE("fetch/fetchFromSet.pec")


