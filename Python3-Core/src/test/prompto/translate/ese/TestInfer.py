from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestInfer(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testInferDict(self):
        self.compareResourceESE("infer/inferDict.pec")

    def testInferList(self):
        self.compareResourceESE("infer/inferList.pec")

    def testInferSet(self):
        self.compareResourceESE("infer/inferSet.pec")


