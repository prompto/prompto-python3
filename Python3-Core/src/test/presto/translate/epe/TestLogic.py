from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLogic(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceEPE("logic/andBoolean.e")

    def testNotBoolean(self):
        self.compareResourceEPE("logic/notBoolean.e")

    def testOrBoolean(self):
        self.compareResourceEPE("logic/orBoolean.e")


