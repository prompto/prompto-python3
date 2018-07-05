from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestWidget(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinimal(self):
        self.compareResourceEOE("widget/minimal.pec")

    def testNative(self):
        self.compareResourceEOE("widget/native.pec")


