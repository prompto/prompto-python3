from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestFetch(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFetchFromList(self):
        self.compareResourceEOE("fetch/fetchFromList.pec")

    def testFetchFromSet(self):
        self.compareResourceEOE("fetch/fetchFromSet.pec")


