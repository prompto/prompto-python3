from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLazy(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceOPO("lazy/cyclic.o")

    def testDict(self):
        self.compareResourceOPO("lazy/dict.o")

    def testList(self):
        self.compareResourceOPO("lazy/list.o")

    def testSet(self):
        self.compareResourceOPO("lazy/set.o")

    def testTransient(self):
        self.compareResourceOPO("lazy/transient.o")


