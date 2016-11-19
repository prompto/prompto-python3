from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestIssues(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinimal(self):
        self.compareResourceEME("issues/minimal.pec")


