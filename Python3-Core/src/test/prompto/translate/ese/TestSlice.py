from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSlice(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceESE("slice/sliceList.pec")

    def testSliceRange(self):
        self.compareResourceESE("slice/sliceRange.pec")

    def testSliceText(self):
        self.compareResourceESE("slice/sliceText.pec")


