from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceOEO("resource/badRead.poc")

    def testBadResource(self):
        self.compareResourceOEO("resource/badResource.poc")

    def testBadWrite(self):
        self.compareResourceOEO("resource/badWrite.poc")

    def testReadResource(self):
        self.compareResourceOEO("resource/readResource.poc")

    def testReadWithResource(self):
        self.compareResourceOEO("resource/readWithResource.poc")

    def testWriteResource(self):
        self.compareResourceOEO("resource/writeResource.poc")

    def testWriteWithResource(self):
        self.compareResourceOEO("resource/writeWithResource.poc")


