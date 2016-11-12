from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestInfer(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testInferDict(self):
        self.compareResourceEOE("infer/inferDict.pec")

    def testInferList(self):
        self.compareResourceEOE("infer/inferList.pec")

    def testInferSet(self):
        self.compareResourceEOE("infer/inferSet.pec")


