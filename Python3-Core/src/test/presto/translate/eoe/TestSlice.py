from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSlice(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceEOE("slice/sliceList.e")

    def testSliceRange(self):
        self.compareResourceEOE("slice/sliceRange.e")

    def testSliceText(self):
        self.compareResourceEOE("slice/sliceText.e")


