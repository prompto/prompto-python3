from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLazy(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCyclic(self):
        self.compareResourceOMO("lazy/cyclic.poc")

    def testDict(self):
        self.compareResourceOMO("lazy/dict.poc")

    def testList(self):
        self.compareResourceOMO("lazy/list.poc")

    def testSet(self):
        self.compareResourceOMO("lazy/set.poc")

    def testTransient(self):
        self.compareResourceOMO("lazy/transient.poc")


