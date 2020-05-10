from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDeepItem(self):
        self.checkOutput("documents/deepItem.poc")

    def testDeepMember(self):
        self.checkOutput("documents/deepMember.poc")

    def testInstance(self):
        self.checkOutput("documents/instance.poc")

    def testItem(self):
        self.checkOutput("documents/item.poc")

    def testLiteral(self):
        self.checkOutput("documents/literal.poc")

    def testMember(self):
        self.checkOutput("documents/member.poc")


