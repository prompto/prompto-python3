from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestFilter(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFilterFromList(self):
        self.compareResourceOSO("filter/filterFromList.poc")

    def testFilterFromSet(self):
        self.compareResourceOSO("filter/filterFromSet.poc")


