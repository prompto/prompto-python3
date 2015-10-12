from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLazy(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceEOE("lazy/cyclic.pec")

    def testDict(self):
        self.compareResourceEOE("lazy/dict.pec")

    def testList(self):
        self.compareResourceEOE("lazy/list.pec")

    def testSet(self):
        self.compareResourceEOE("lazy/set.pec")

    def testTransient(self):
        self.compareResourceEOE("lazy/transient.pec")


