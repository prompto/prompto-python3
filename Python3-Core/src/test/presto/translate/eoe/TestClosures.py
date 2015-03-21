from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestClosures(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceEOE("closures/globalClosureNoArg.e")

    def testGlobalClosureWithArg(self):
        self.compareResourceEOE("closures/globalClosureWithArg.e")

    def testInstanceClosureNoArg(self):
        self.compareResourceEOE("closures/instanceClosureNoArg.e")


