from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestClosures(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGlobalClosureNoArg(self):
        self.checkOutput("closures/globalClosureNoArg.e")

    def testGlobalClosureWithArg(self):
        self.checkOutput("closures/globalClosureWithArg.e")

    def testInstanceClosureNoArg(self):
        self.checkOutput("closures/instanceClosureNoArg.e")


