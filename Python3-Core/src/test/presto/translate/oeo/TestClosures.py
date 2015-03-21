from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestClosures(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceOEO("closures/globalClosureNoArg.o")

    def testGlobalClosureWithArg(self):
        self.compareResourceOEO("closures/globalClosureWithArg.o")

    def testInstanceClosureNoArg(self):
        self.compareResourceOEO("closures/instanceClosureNoArg.o")


