from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestSlice(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSliceList(self):
        self.checkOutput("slice/sliceList.poc")

    def testSliceRange(self):
        self.checkOutput("slice/sliceRange.poc")

    def testSliceText(self):
        self.checkOutput("slice/sliceText.poc")


