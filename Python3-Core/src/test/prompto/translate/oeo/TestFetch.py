# generated: 2015-07-05T23:01:01.806
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestFetch(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFetchFromList(self):
        self.compareResourceOEO("fetch/fetchFromList.poc")

    def testFetchFromSet(self):
        self.compareResourceOEO("fetch/fetchFromSet.poc")


