from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBlob(self):
        self.compareResourceEME("documents/blob.pec")

    def testDeepItem(self):
        self.compareResourceEME("documents/deepItem.pec")

    def testDeepMember(self):
        self.compareResourceEME("documents/deepMember.pec")

    def testInstance(self):
        self.compareResourceEME("documents/instance.pec")

    def testItem(self):
        self.compareResourceEME("documents/item.pec")

    def testLiteral(self):
        self.compareResourceEME("documents/literal.pec")

    def testMember(self):
        self.compareResourceEME("documents/member.pec")

    def testNamedItem(self):
        self.compareResourceEME("documents/namedItem.pec")


