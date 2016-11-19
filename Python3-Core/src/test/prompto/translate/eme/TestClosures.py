from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestClosures(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGlobalClosureNoArg(self):
        self.compareResourceEME("closures/globalClosureNoArg.pec")

    def testGlobalClosureWithArg(self):
        self.compareResourceEME("closures/globalClosureWithArg.pec")

    def testInstanceClosureNoArg(self):
        self.compareResourceEME("closures/instanceClosureNoArg.pec")

    def testParameterClosure(self):
        self.compareResourceEME("closures/parameterClosure.pec")


