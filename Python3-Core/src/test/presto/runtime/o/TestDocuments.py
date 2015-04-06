from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDeepItem(self):
        self.checkOutput("documents/deepItem.poc")

    def testDeepVariable(self):
        self.checkOutput("documents/deepVariable.poc")

    def testItem(self):
        self.checkOutput("documents/item.poc")

    def testVariable(self):
        self.checkOutput("documents/variable.poc")


