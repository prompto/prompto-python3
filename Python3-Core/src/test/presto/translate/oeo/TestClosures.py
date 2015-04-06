from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestClosures(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceOEO("closures/globalClosureNoArg.poc")

    def testGlobalClosureWithArg(self):
        self.compareResourceOEO("closures/globalClosureWithArg.poc")

    def testInstanceClosureNoArg(self):
        self.compareResourceOEO("closures/instanceClosureNoArg.poc")


