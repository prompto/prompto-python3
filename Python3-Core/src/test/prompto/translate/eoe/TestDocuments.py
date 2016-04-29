from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBlob(self):
        self.compareResourceEOE("documents/blob.pec")

    def testDeepItem(self):
        self.compareResourceEOE("documents/deepItem.pec")

    def testDeepVariable(self):
        self.compareResourceEOE("documents/deepVariable.pec")

    def testItem(self):
        self.compareResourceEOE("documents/item.pec")

    def testNamedItem(self):
        self.compareResourceEOE("documents/namedItem.pec")

    def testVariable(self):
        self.compareResourceEOE("documents/variable.pec")


