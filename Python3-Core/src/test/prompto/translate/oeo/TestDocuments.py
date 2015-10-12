from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceOEO("documents/deepItem.poc")

    def testDeepVariable(self):
        self.compareResourceOEO("documents/deepVariable.poc")

    def testItem(self):
        self.compareResourceOEO("documents/item.poc")

    def testVariable(self):
        self.compareResourceOEO("documents/variable.poc")


