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

    def testDeepVariable(self):
        self.checkOutput("documents/deepVariable.pec")

    def testItem(self):
        self.checkOutput("documents/item.pec")

    def testNamedItem(self):
        self.checkOutput("documents/namedItem.pec")

    def testVariable(self):
        self.checkOutput("documents/variable.pec")


