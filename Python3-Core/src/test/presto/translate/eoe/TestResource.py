from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestResource(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceEOE("resource/badRead.e")

    def testBadResource(self):
        self.compareResourceEOE("resource/badResource.e")

    def testBadWrite(self):
        self.compareResourceEOE("resource/badWrite.e")

    def testReadResource(self):
        self.compareResourceEOE("resource/readResource.e")

    def testReadWithResource(self):
        self.compareResourceEOE("resource/readWithResource.e")

    def testWriteResource(self):
        self.compareResourceEOE("resource/writeResource.e")

    def testWriteWithResource(self):
        self.compareResourceEOE("resource/writeWithResource.e")


