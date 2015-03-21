from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLazy(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceEOE("lazy/cyclic.e")

    def testDict(self):
        self.compareResourceEOE("lazy/dict.e")

    def testList(self):
        self.compareResourceEOE("lazy/list.e")

    def testSet(self):
        self.compareResourceEOE("lazy/set.e")

    def testTransient(self):
        self.compareResourceEOE("lazy/transient.e")


