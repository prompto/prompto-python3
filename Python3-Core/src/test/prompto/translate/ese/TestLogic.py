from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLogic(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceESE("logic/andBoolean.pec")

    def testNotBoolean(self):
        self.compareResourceESE("logic/notBoolean.pec")

    def testOrBoolean(self):
        self.compareResourceESE("logic/orBoolean.pec")


