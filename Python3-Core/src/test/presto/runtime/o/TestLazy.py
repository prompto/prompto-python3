from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestLazy(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCyclic(self):
        self.checkOutput("lazy/cyclic.poc")

    def testDict(self):
        self.checkOutput("lazy/dict.poc")

    def testList(self):
        self.checkOutput("lazy/list.poc")

    def testSet(self):
        self.checkOutput("lazy/set.poc")

    def testTransient(self):
        self.checkOutput("lazy/transient.poc")


