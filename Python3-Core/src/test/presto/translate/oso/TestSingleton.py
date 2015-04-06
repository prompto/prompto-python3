from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceOSO("singleton/attribute.poc")

    def testMember(self):
        self.compareResourceOSO("singleton/member.poc")


