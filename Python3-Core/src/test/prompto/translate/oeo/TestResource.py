from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReadInDoWhile(self):
        self.compareResourceOEO("resource/readInDoWhile.poc")

    def testReadInForEach(self):
        self.compareResourceOEO("resource/readInForEach.poc")

    def testReadInIf(self):
        self.compareResourceOEO("resource/readInIf.poc")

    def testReadInWhile(self):
        self.compareResourceOEO("resource/readInWhile.poc")

    def testReadResource(self):
        self.compareResourceOEO("resource/readResource.poc")

    def testReadResourceThen(self):
        self.compareResourceOEO("resource/readResourceThen.poc")

    def testReadWithResource(self):
        self.compareResourceOEO("resource/readWithResource.poc")

    def testWriteResource(self):
        self.compareResourceOEO("resource/writeResource.poc")

    def testWriteResourceThen(self):
        self.compareResourceOEO("resource/writeResourceThen.poc")

    def testWriteWithResource(self):
        self.compareResourceOEO("resource/writeWithResource.poc")


