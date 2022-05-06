from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestRecursive(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMutuallyRecursive(self):
        self.checkOutput("recursive/mutuallyRecursive.poc")

    def testRecursive(self):
        self.checkOutput("recursive/recursive.poc")


