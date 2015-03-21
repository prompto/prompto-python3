from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestClosures(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceEPE("closures/globalClosureNoArg.e")

    def testGlobalClosureWithArg(self):
        self.compareResourceEPE("closures/globalClosureWithArg.e")

    def testInstanceClosureNoArg(self):
        self.compareResourceEPE("closures/instanceClosureNoArg.e")


