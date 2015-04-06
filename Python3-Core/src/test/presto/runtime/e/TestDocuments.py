from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDeepItem(self):
        self.checkOutput("documents/deepItem.pec")

    def testDeepVariable(self):
        self.checkOutput("documents/deepVariable.pec")

    def testItem(self):
        self.checkOutput("documents/item.pec")

    def testVariable(self):
        self.checkOutput("documents/variable.pec")


