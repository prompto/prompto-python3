from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLazy(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceEME("lazy/cyclic.pec")

    def testDict(self):
        self.compareResourceEME("lazy/dict.pec")

    def testList(self):
        self.compareResourceEME("lazy/list.pec")

    def testSet(self):
        self.compareResourceEME("lazy/set.pec")

    def testTransient(self):
        self.compareResourceEME("lazy/transient.pec")


