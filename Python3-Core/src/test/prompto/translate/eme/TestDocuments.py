from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBlob(self):
        self.compareResourceEME("documents/blob.pec")

    def testDeepItem(self):
        self.compareResourceEME("documents/deepItem.pec")

    def testDeepVariable(self):
        self.compareResourceEME("documents/deepVariable.pec")

    def testItem(self):
        self.compareResourceEME("documents/item.pec")

    def testNamedItem(self):
        self.compareResourceEME("documents/namedItem.pec")

    def testVariable(self):
        self.compareResourceEME("documents/variable.pec")


