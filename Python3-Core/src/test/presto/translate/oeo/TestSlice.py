from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSlice(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceOEO("slice/sliceList.o")

    def testSliceRange(self):
        self.compareResourceOEO("slice/sliceRange.o")

    def testSliceText(self):
        self.compareResourceOEO("slice/sliceText.o")


