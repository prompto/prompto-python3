from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestClosures(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceOPO("closures/globalClosureNoArg.o")

    def testGlobalClosureWithArg(self):
        self.compareResourceOPO("closures/globalClosureWithArg.o")

    def testInstanceClosureNoArg(self):
        self.compareResourceOPO("closures/instanceClosureNoArg.o")


