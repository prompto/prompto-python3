from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestInfer(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testInferDict(self):
        self.checkOutput("infer/inferDict.pec")

    def testInferList(self):
        self.checkOutput("infer/inferList.pec")

    def testInferSet(self):
        self.checkOutput("infer/inferSet.pec")


