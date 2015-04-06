from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLogic(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceOSO("logic/andBoolean.poc")

    def testNotBoolean(self):
        self.compareResourceOSO("logic/notBoolean.poc")

    def testOrBoolean(self):
        self.compareResourceOSO("logic/orBoolean.poc")


