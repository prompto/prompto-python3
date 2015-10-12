from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestFetch(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testFetchFromList(self):
        self.checkOutput("fetch/fetchFromList.pec")

    def testFetchFromSet(self):
        self.checkOutput("fetch/fetchFromSet.pec")


