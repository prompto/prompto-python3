from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLogic(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceOMO("logic/andBoolean.poc")

    def testNotBoolean(self):
        self.compareResourceOMO("logic/notBoolean.poc")

    def testOrBoolean(self):
        self.compareResourceOMO("logic/orBoolean.poc")


