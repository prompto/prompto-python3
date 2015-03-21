from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLazy(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceOEO("lazy/cyclic.o")

    def testDict(self):
        self.compareResourceOEO("lazy/dict.o")

    def testList(self):
        self.compareResourceOEO("lazy/list.o")

    def testSet(self):
        self.compareResourceOEO("lazy/set.o")

    def testTransient(self):
        self.compareResourceOEO("lazy/transient.o")


