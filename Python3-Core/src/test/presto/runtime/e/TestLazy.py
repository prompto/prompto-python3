from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestLazy(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCyclic(self):
        self.checkOutput("lazy/cyclic.pec")

    def testDict(self):
        self.checkOutput("lazy/dict.pec")

    def testList(self):
        self.checkOutput("lazy/list.pec")

    def testSet(self):
        self.checkOutput("lazy/set.pec")

    def testTransient(self):
        self.checkOutput("lazy/transient.pec")


