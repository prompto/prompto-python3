# generated: 2015-07-05T23:01:01.745
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


