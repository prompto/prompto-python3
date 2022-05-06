from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestRecursive(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMutuallyRecursive(self):
        self.compareResourceOMO("recursive/mutuallyRecursive.poc")

    def testRecursive(self):
        self.compareResourceOMO("recursive/recursive.poc")


