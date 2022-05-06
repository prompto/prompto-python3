from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestRecursive(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMutuallyRecursive(self):
        self.compareResourceOEO("recursive/mutuallyRecursive.poc")

    def testRecursive(self):
        self.compareResourceOEO("recursive/recursive.poc")


