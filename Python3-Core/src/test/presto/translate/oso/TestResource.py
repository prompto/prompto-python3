from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceOSO("resource/badRead.poc")

    def testBadResource(self):
        self.compareResourceOSO("resource/badResource.poc")

    def testBadWrite(self):
        self.compareResourceOSO("resource/badWrite.poc")

    def testReadResource(self):
        self.compareResourceOSO("resource/readResource.poc")

    def testReadWithResource(self):
        self.compareResourceOSO("resource/readWithResource.poc")

    def testWriteResource(self):
        self.compareResourceOSO("resource/writeResource.poc")

    def testWriteWithResource(self):
        self.compareResourceOSO("resource/writeWithResource.poc")


