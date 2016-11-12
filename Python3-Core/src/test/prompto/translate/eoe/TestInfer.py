from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestInfer(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testInferList(self):
        self.compareResourceEOE("infer/inferList.pec")


