from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestProblems(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAbstract(self):
        self.compareResourceOEO("problems/abstract.poc")


