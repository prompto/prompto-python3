from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestLazy(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCyclic(self):
        self.checkOutput("lazy/cyclic.e")

    def testDict(self):
        self.checkOutput("lazy/dict.e")

    def testList(self):
        self.checkOutput("lazy/list.e")

    def testSet(self):
        self.checkOutput("lazy/set.e")

    def testTransient(self):
        self.checkOutput("lazy/transient.e")


