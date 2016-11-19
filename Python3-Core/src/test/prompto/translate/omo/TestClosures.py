from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestClosures(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceOMO("closures/globalClosureNoArg.poc")

    def testGlobalClosureWithArg(self):
        self.compareResourceOMO("closures/globalClosureWithArg.poc")

    def testInstanceClosureNoArg(self):
        self.compareResourceOMO("closures/instanceClosureNoArg.poc")


