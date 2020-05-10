from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDocuments(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBlob(self):
        self.compareResourceEOE("documents/blob.pec")

    def testDeepItem(self):
        self.compareResourceEOE("documents/deepItem.pec")

    def testDeepMember(self):
        self.compareResourceEOE("documents/deepMember.pec")

    def testInstance(self):
        self.compareResourceEOE("documents/instance.pec")

    def testItem(self):
        self.compareResourceEOE("documents/item.pec")

    def testLiteral(self):
        self.compareResourceEOE("documents/literal.pec")

    def testMember(self):
        self.compareResourceEOE("documents/member.pec")

    def testNamedItem(self):
        self.compareResourceEOE("documents/namedItem.pec")


