from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceOSO("documents/deepItem.poc")

    def testDeepVariable(self):
        self.compareResourceOSO("documents/deepVariable.poc")

    def testItem(self):
        self.compareResourceOSO("documents/item.poc")

    def testVariable(self):
        self.compareResourceOSO("documents/variable.poc")


