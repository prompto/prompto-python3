from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSelf(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSelfAsParameter(self):
        self.compareResourceOEO("self/selfAsParameter.o")

    def testSelfMember(self):
        self.compareResourceOEO("self/selfMember.o")


