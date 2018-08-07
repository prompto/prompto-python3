from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceOEO("documents/deepItem.poc")

    def testDeepMember(self):
        self.compareResourceOEO("documents/deepMember.poc")

    def testItem(self):
        self.compareResourceOEO("documents/item.poc")

    def testLiteral(self):
        self.compareResourceOEO("documents/literal.poc")

    def testMember(self):
        self.compareResourceOEO("documents/member.poc")


