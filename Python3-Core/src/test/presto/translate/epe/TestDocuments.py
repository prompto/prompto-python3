from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceEPE("documents/deepItem.e")

    def testDeepVariable(self):
        self.compareResourceEPE("documents/deepVariable.e")

    def testItem(self):
        self.compareResourceEPE("documents/item.e")

    def testVariable(self):
        self.compareResourceEPE("documents/variable.e")


