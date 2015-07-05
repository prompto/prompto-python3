# generated: 2015-07-05T23:01:01.940
from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAttribute(self):
        self.checkOutput("singleton/attribute.pec")

    def testMember(self):
        self.checkOutput("singleton/member.pec")


