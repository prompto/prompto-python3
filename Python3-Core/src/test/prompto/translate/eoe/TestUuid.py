from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestUuid(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testUuid(self):
        self.compareResourceEOE("uuid/uuid.pec")


