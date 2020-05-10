from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestDocuments(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDeepItem(self):
        self.compareResourceOMO("documents/deepItem.poc")

    def testDeepMember(self):
        self.compareResourceOMO("documents/deepMember.poc")

    def testInstance(self):
        self.compareResourceOMO("documents/instance.poc")

    def testItem(self):
        self.compareResourceOMO("documents/item.poc")

    def testLiteral(self):
        self.compareResourceOMO("documents/literal.poc")

    def testMember(self):
        self.compareResourceOMO("documents/member.poc")


