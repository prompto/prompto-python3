from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestResource(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceEPE("resource/badRead.e")

    def testBadResource(self):
        self.compareResourceEPE("resource/badResource.e")

    def testBadWrite(self):
        self.compareResourceEPE("resource/badWrite.e")

    def testReadResource(self):
        self.compareResourceEPE("resource/readResource.e")

    def testReadWithResource(self):
        self.compareResourceEPE("resource/readWithResource.e")

    def testWriteResource(self):
        self.compareResourceEPE("resource/writeResource.e")

    def testWriteWithResource(self):
        self.compareResourceEPE("resource/writeWithResource.e")


