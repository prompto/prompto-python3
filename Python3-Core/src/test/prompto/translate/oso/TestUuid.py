from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestUuid(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testUuid(self):
        self.compareResourceOSO("uuid/uuid.poc")


