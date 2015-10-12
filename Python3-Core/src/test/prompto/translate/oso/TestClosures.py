from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestClosures(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceOSO("closures/globalClosureNoArg.poc")

    def testGlobalClosureWithArg(self):
        self.compareResourceOSO("closures/globalClosureWithArg.poc")

    def testInstanceClosureNoArg(self):
        self.compareResourceOSO("closures/instanceClosureNoArg.poc")


