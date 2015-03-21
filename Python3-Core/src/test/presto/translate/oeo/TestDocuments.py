from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceOEO("documents/deepItem.o")

    def testDeepVariable(self):
        self.compareResourceOEO("documents/deepVariable.o")

    def testItem(self):
        self.compareResourceOEO("documents/item.o")

    def testVariable(self):
        self.compareResourceOEO("documents/variable.o")


