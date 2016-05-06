from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestResourceError(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceEOE("resourceError/badRead.pec")

    def testBadResource(self):
        self.compareResourceEOE("resourceError/badResource.pec")

    def testBadWrite(self):
        self.compareResourceEOE("resourceError/badWrite.pec")


