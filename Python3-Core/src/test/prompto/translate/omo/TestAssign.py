from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAssign(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDictEntry(self):
        self.compareResourceOMO("assign/dictEntry.poc")


