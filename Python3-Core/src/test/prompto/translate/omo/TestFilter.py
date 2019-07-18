from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestFilter(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFilterFromIterable(self):
        self.compareResourceOMO("filter/filterFromIterable.poc")

    def testFilterFromList(self):
        self.compareResourceOMO("filter/filterFromList.poc")

    def testFilterFromSet(self):
        self.compareResourceOMO("filter/filterFromSet.poc")


