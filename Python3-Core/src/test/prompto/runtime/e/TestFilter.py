from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestFilter(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testFilterFromCursor(self):
        self.checkOutput("filter/filterFromCursor.pec")

    def testFilterFromList(self):
        self.checkOutput("filter/filterFromList.pec")

    def testFilterFromSet(self):
        self.checkOutput("filter/filterFromSet.pec")


