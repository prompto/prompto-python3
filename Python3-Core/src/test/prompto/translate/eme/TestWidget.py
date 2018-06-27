from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestWidget(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinimal(self):
        self.compareResourceEME("widget/minimal.pec")


