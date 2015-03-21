from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestSlice(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSliceList(self):
        self.checkOutput("slice/sliceList.e")

    def testSliceRange(self):
        self.checkOutput("slice/sliceRange.e")

    def testSliceText(self):
        self.checkOutput("slice/sliceText.e")


