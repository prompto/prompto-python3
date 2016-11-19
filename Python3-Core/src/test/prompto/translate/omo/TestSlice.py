from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSlice(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceOMO("slice/sliceList.poc")

    def testSliceRange(self):
        self.compareResourceOMO("slice/sliceRange.poc")

    def testSliceText(self):
        self.compareResourceOMO("slice/sliceText.poc")


