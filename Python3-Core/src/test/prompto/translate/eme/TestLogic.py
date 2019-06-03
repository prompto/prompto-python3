from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLogic(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceEME("logic/andBoolean.pec")

    def testNotBoolean(self):
        self.compareResourceEME("logic/notBoolean.pec")

    def testOrBoolean(self):
        self.compareResourceEME("logic/orBoolean.pec")

    def testRightSkipped(self):
        self.compareResourceEME("logic/rightSkipped.pec")


