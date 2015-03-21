from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceOPO("singleton/attribute.o")

    def testMember(self):
        self.compareResourceOPO("singleton/member.o")


