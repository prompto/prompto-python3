from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestFetch(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFetchFromList(self):
        self.compareResourceOPO("fetch/fetchFromList.o")

    def testFetchFromSet(self):
        self.compareResourceOPO("fetch/fetchFromSet.o")


