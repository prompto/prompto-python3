from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestClosures(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGlobalClosureNoArg(self):
        self.checkOutput("closures/globalClosureNoArg.poc")

    def testGlobalClosureWithArg(self):
        self.checkOutput("closures/globalClosureWithArg.poc")

    def testInstanceClosureNoArg(self):
        self.checkOutput("closures/instanceClosureNoArg.poc")


