from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceOEO("resource/badRead.o")

    def testBadResource(self):
        self.compareResourceOEO("resource/badResource.o")

    def testBadWrite(self):
        self.compareResourceOEO("resource/badWrite.o")

    def testReadResource(self):
        self.compareResourceOEO("resource/readResource.o")

    def testReadWithResource(self):
        self.compareResourceOEO("resource/readWithResource.o")

    def testWriteResource(self):
        self.compareResourceOEO("resource/writeResource.o")

    def testWriteWithResource(self):
        self.compareResourceOEO("resource/writeWithResource.o")


