from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestResourceError(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceESE("resourceError/badRead.pec")

    def testBadResource(self):
        self.compareResourceESE("resourceError/badResource.pec")

    def testBadWrite(self):
        self.compareResourceESE("resourceError/badWrite.pec")


