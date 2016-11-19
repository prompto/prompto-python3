from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestInfer(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testInferDict(self):
        self.compareResourceEME("infer/inferDict.pec")

    def testInferList(self):
        self.compareResourceEME("infer/inferList.pec")

    def testInferSet(self):
        self.compareResourceEME("infer/inferSet.pec")


