from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestLazy(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCyclic(self):
        self.checkOutput("lazy/cyclic.o")

    def testDict(self):
        self.checkOutput("lazy/dict.o")

    def testList(self):
        self.checkOutput("lazy/list.o")

    def testSet(self):
        self.checkOutput("lazy/set.o")

    def testTransient(self):
        self.checkOutput("lazy/transient.o")


