from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResourceError(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceOSO("resourceError/badRead.poc")

    def testBadResource(self):
        self.compareResourceOSO("resourceError/badResource.poc")

    def testBadWrite(self):
        self.compareResourceOSO("resourceError/badWrite.poc")


