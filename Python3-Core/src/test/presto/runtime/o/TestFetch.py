from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestFetch(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testFetchFromList(self):
        self.checkOutput("fetch/fetchFromList.poc")

    def testFetchFromSet(self):
        self.checkOutput("fetch/fetchFromSet.poc")


