from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLazy(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceESE("lazy/cyclic.pec")

    def testDict(self):
        self.compareResourceESE("lazy/dict.pec")

    def testList(self):
        self.compareResourceESE("lazy/list.pec")

    def testSet(self):
        self.compareResourceESE("lazy/set.pec")

    def testTransient(self):
        self.compareResourceESE("lazy/transient.pec")


