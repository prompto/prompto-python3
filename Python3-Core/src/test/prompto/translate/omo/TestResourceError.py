from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResourceError(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceOMO("resourceError/badRead.poc")

    def testBadResource(self):
        self.compareResourceOMO("resourceError/badResource.poc")

    def testBadWrite(self):
        self.compareResourceOMO("resourceError/badWrite.poc")


