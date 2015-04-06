from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestFetch(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFetchFromList(self):
        self.compareResourceOSO("fetch/fetchFromList.poc")

    def testFetchFromSet(self):
        self.compareResourceOSO("fetch/fetchFromSet.poc")


