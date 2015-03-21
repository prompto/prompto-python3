from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLazy(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceEPE("lazy/cyclic.e")

    def testDict(self):
        self.compareResourceEPE("lazy/dict.e")

    def testList(self):
        self.compareResourceEPE("lazy/list.e")

    def testSet(self):
        self.compareResourceEPE("lazy/set.e")

    def testTransient(self):
        self.compareResourceEPE("lazy/transient.e")


