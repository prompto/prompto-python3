from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSlice(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceEOE("slice/sliceList.pec")

    def testSliceRange(self):
        self.compareResourceEOE("slice/sliceRange.pec")

    def testSliceText(self):
        self.compareResourceEOE("slice/sliceText.pec")


