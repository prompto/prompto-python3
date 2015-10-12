from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestRecord(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testRecord(self):
        self.compareResourceEOE("record/record.pec")


