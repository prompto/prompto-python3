from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestResourceError(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceEME("resourceError/badRead.pec")

    def testBadResource(self):
        self.compareResourceEME("resourceError/badResource.pec")

    def testBadWrite(self):
        self.compareResourceEME("resourceError/badWrite.pec")


