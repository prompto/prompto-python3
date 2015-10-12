from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLazy(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceOEO("lazy/cyclic.poc")

    def testDict(self):
        self.compareResourceOEO("lazy/dict.poc")

    def testList(self):
        self.compareResourceOEO("lazy/list.poc")

    def testSet(self):
        self.compareResourceOEO("lazy/set.poc")

    def testTransient(self):
        self.compareResourceOEO("lazy/transient.poc")


