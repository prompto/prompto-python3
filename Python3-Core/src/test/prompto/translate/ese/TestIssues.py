# generated: 2015-07-05T23:01:01.832
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestIssues(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinimal(self):
        self.compareResourceESE("issues/minimal.pec")


