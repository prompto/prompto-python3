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

    def testRightSkipped(self):
        self.compareResourceEOE("logic/rightSkipped.pec")


