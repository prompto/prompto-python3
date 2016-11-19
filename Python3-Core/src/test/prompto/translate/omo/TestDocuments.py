from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceOMO("documents/deepItem.poc")

    def testDeepVariable(self):
        self.compareResourceOMO("documents/deepVariable.poc")

    def testItem(self):
        self.compareResourceOMO("documents/item.poc")

    def testVariable(self):
        self.compareResourceOMO("documents/variable.poc")


