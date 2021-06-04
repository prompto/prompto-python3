from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReadInDoWhile(self):
        self.compareResourceOMO("resource/readInDoWhile.poc")

    def testReadInForEach(self):
        self.compareResourceOMO("resource/readInForEach.poc")

    def testReadInIf(self):
        self.compareResourceOMO("resource/readInIf.poc")

    def testReadInWhile(self):
        self.compareResourceOMO("resource/readInWhile.poc")

    def testReadResource(self):
        self.compareResourceOMO("resource/readResource.poc")

    def testReadResourceThen(self):
        self.compareResourceOMO("resource/readResourceThen.poc")

    def testReadWithResource(self):
        self.compareResourceOMO("resource/readWithResource.poc")

    def testWriteResource(self):
        self.compareResourceOMO("resource/writeResource.poc")

    def testWriteResourceThen(self):
        self.compareResourceOMO("resource/writeResourceThen.poc")

    def testWriteWithResource(self):
        self.compareResourceOMO("resource/writeWithResource.poc")


