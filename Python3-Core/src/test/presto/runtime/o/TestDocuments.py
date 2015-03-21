from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDeepItem(self):
        self.checkOutput("documents/deepItem.o")

    def testDeepVariable(self):
        self.checkOutput("documents/deepVariable.o")

    def testItem(self):
        self.checkOutput("documents/item.o")

    def testVariable(self):
        self.checkOutput("documents/variable.o")


