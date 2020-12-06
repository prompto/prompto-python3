from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceOMO("singleton/attribute.poc")

    def testDictionary(self):
        self.compareResourceOMO("singleton/dictionary.poc")

    def testInitialize(self):
        self.compareResourceOMO("singleton/initialize.poc")

    def testInternal(self):
        self.compareResourceOMO("singleton/internal.poc")

    def testMember(self):
        self.compareResourceOMO("singleton/member.poc")


