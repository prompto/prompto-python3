from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestFilter(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testFilterFromList(self):
        self.checkOutput("filter/filterFromList.poc")

    def testFilterFromSet(self):
        self.checkOutput("filter/filterFromSet.poc")


