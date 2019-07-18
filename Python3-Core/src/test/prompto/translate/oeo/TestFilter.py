from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestFilter(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFilterFromIterable(self):
        self.compareResourceOEO("filter/filterFromIterable.poc")

    def testFilterFromList(self):
        self.compareResourceOEO("filter/filterFromList.poc")

    def testFilterFromSet(self):
        self.compareResourceOEO("filter/filterFromSet.poc")


