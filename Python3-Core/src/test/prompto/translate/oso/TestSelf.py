from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSelf(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSelfAsParameter(self):
        self.compareResourceOSO("self/selfAsParameter.poc")

    def testSelfMember(self):
        self.compareResourceOSO("self/selfMember.poc")


