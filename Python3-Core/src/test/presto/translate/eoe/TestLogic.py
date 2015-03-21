from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLogic(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAndBoolean(self):
        self.compareResourceEOE("logic/andBoolean.e")

    def testNotBoolean(self):
        self.compareResourceEOE("logic/notBoolean.e")

    def testOrBoolean(self):
        self.compareResourceEOE("logic/orBoolean.e")


