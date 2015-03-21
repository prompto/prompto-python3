from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestSelf(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSelfAsParameter(self):
        self.checkOutput("self/selfAsParameter.e")

    def testSelfMember(self):
        self.checkOutput("self/selfMember.e")


