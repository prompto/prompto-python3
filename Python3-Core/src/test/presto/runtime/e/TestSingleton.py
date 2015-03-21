from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAttribute(self):
        self.checkOutput("singleton/attribute.e")

    def testMember(self):
        self.checkOutput("singleton/member.e")


