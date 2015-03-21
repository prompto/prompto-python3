from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSlice(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSliceList(self):
        self.compareResourceOPO("slice/sliceList.o")

    def testSliceRange(self):
        self.compareResourceOPO("slice/sliceRange.o")

    def testSliceText(self):
        self.compareResourceOPO("slice/sliceText.o")


