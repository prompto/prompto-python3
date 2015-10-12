from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSlice(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceOEO("slice/sliceList.poc")

    def testSliceRange(self):
        self.compareResourceOEO("slice/sliceRange.poc")

    def testSliceText(self):
        self.compareResourceOEO("slice/sliceText.poc")


