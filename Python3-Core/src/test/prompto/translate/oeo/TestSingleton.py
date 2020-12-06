from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceOEO("singleton/attribute.poc")

    def testDictionary(self):
        self.compareResourceOEO("singleton/dictionary.poc")

    def testInitialize(self):
        self.compareResourceOEO("singleton/initialize.poc")

    def testInternal(self):
        self.compareResourceOEO("singleton/internal.poc")

    def testMember(self):
        self.compareResourceOEO("singleton/member.poc")


