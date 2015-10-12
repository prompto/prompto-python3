from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestClosures(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceESE("closures/globalClosureNoArg.pec")

    def testGlobalClosureWithArg(self):
        self.compareResourceESE("closures/globalClosureWithArg.pec")

    def testInstanceClosureNoArg(self):
        self.compareResourceESE("closures/instanceClosureNoArg.pec")


