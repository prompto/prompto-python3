from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceOPO("documents/deepItem.o")

    def testDeepVariable(self):
        self.compareResourceOPO("documents/deepVariable.o")

    def testItem(self):
        self.compareResourceOPO("documents/item.o")

    def testVariable(self):
        self.compareResourceOPO("documents/variable.o")


