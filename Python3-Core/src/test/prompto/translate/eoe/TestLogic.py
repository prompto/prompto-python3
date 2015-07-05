# generated: 2015-07-05T23:01:01.853
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLogic(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceEOE("logic/andBoolean.pec")

    def testNotBoolean(self):
        self.compareResourceEOE("logic/notBoolean.pec")

    def testOrBoolean(self):
        self.compareResourceEOE("logic/orBoolean.pec")


