from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestResource(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceESE("resource/badRead.pec")

    def testBadResource(self):
        self.compareResourceESE("resource/badResource.pec")

    def testBadWrite(self):
        self.compareResourceESE("resource/badWrite.pec")

    def testReadResource(self):
        self.compareResourceESE("resource/readResource.pec")

    def testReadWithResource(self):
        self.compareResourceESE("resource/readWithResource.pec")

    def testWriteResource(self):
        self.compareResourceESE("resource/writeResource.pec")

    def testWriteWithResource(self):
        self.compareResourceESE("resource/writeWithResource.pec")


