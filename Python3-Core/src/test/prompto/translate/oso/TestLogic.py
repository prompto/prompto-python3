# generated: 2015-07-05T23:01:01.857
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLogic(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceOSO("logic/andBoolean.poc")

    def testNotBoolean(self):
        self.compareResourceOSO("logic/notBoolean.poc")

    def testOrBoolean(self):
        self.compareResourceOSO("logic/orBoolean.poc")


