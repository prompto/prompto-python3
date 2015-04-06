from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestIssues(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinimal(self):
        self.compareResourceESE("issues/minimal.pec")


