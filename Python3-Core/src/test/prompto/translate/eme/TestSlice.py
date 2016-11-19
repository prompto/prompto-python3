from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSlice(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceEME("slice/sliceList.pec")

    def testSliceRange(self):
        self.compareResourceEME("slice/sliceRange.pec")

    def testSliceText(self):
        self.compareResourceEME("slice/sliceText.pec")


