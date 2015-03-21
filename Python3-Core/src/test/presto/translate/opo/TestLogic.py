from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLogic(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceOPO("logic/andBoolean.o")

    def testNotBoolean(self):
        self.compareResourceOPO("logic/notBoolean.o")

    def testOrBoolean(self):
        self.compareResourceOPO("logic/orBoolean.o")


