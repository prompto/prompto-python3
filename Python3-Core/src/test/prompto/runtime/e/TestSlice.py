from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSlice(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSliceList(self):
        self.checkOutput("slice/sliceList.pec")

    def testSliceRange(self):
        self.checkOutput("slice/sliceRange.pec")

    def testSliceText(self):
        self.checkOutput("slice/sliceText.pec")


