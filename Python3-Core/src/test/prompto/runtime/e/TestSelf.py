# generated: 2015-07-05T23:01:01.926
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSelf(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSelfAsParameter(self):
        self.checkOutput("self/selfAsParameter.pec")

    def testSelfMember(self):
        self.checkOutput("self/selfMember.pec")


