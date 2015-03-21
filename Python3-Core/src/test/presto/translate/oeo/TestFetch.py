from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestFetch(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFetchFromList(self):
        self.compareResourceOEO("fetch/fetchFromList.o")

    def testFetchFromSet(self):
        self.compareResourceOEO("fetch/fetchFromSet.o")


