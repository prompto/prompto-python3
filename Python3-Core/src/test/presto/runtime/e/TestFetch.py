from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestFetch(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testFetchFromList(self):
        self.checkOutput("fetch/fetchFromList.e")

    def testFetchFromSet(self):
        self.checkOutput("fetch/fetchFromSet.e")


