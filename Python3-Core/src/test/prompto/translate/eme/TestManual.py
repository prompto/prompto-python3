from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestManual(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testScheduler(self):
        self.compareResourceEME("manual/scheduler.pec")


