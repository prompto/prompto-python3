from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLazy(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceOSO("lazy/cyclic.poc")

    def testDict(self):
        self.compareResourceOSO("lazy/dict.poc")

    def testList(self):
        self.compareResourceOSO("lazy/list.poc")

    def testSet(self):
        self.compareResourceOSO("lazy/set.poc")

    def testTransient(self):
        self.compareResourceOSO("lazy/transient.poc")


