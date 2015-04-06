from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceEOE("documents/deepItem.pec")

    def testDeepVariable(self):
        self.compareResourceEOE("documents/deepVariable.pec")

    def testItem(self):
        self.compareResourceEOE("documents/item.pec")

    def testVariable(self):
        self.compareResourceEOE("documents/variable.pec")


