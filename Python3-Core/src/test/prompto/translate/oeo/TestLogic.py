from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLogic(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceOEO("logic/andBoolean.poc")

    def testNotBoolean(self):
        self.compareResourceOEO("logic/notBoolean.poc")

    def testOrBoolean(self):
        self.compareResourceOEO("logic/orBoolean.poc")

    def testRightSkipped(self):
        self.compareResourceOEO("logic/rightSkipped.poc")


