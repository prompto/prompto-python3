from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testBadRead(self):
        self.compareResourceOPO("resource/badRead.o")

    def testBadResource(self):
        self.compareResourceOPO("resource/badResource.o")

    def testBadWrite(self):
        self.compareResourceOPO("resource/badWrite.o")

    def testReadResource(self):
        self.compareResourceOPO("resource/readResource.o")

    def testReadWithResource(self):
        self.compareResourceOPO("resource/readWithResource.o")

    def testWriteResource(self):
        self.compareResourceOPO("resource/writeResource.o")

    def testWriteWithResource(self):
        self.compareResourceOPO("resource/writeWithResource.o")


