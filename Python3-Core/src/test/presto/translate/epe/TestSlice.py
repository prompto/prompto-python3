from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSlice(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceEPE("slice/sliceList.e")

    def testSliceRange(self):
        self.compareResourceEPE("slice/sliceRange.e")

    def testSliceText(self):
        self.compareResourceEPE("slice/sliceText.e")


