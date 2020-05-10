from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testBlob(self):
        self.checkOutput("documents/blob.pec")

    def testDeepItem(self):
        self.checkOutput("documents/deepItem.pec")

    def testDeepMember(self):
        self.checkOutput("documents/deepMember.pec")

    def testInstance(self):
        self.checkOutput("documents/instance.pec")

    def testItem(self):
        self.checkOutput("documents/item.pec")

    def testLiteral(self):
        self.checkOutput("documents/literal.pec")

    def testMember(self):
        self.checkOutput("documents/member.pec")

    def testNamedItem(self):
        self.checkOutput("documents/namedItem.pec")


