from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceEOE("documents/deepItem.e")

    def testDeepVariable(self):
        self.compareResourceEOE("documents/deepVariable.e")

    def testItem(self):
        self.compareResourceEOE("documents/item.e")

    def testVariable(self):
        self.compareResourceEOE("documents/variable.e")


