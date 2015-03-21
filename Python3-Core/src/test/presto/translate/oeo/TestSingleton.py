from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceOEO("singleton/attribute.o")

    def testMember(self):
        self.compareResourceOEO("singleton/member.o")


