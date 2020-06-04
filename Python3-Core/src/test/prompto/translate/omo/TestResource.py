from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReadResource(self):
        self.compareResourceOMO("resource/readResource.poc")

    def testReadResourceThen(self):
        self.compareResourceOMO("resource/readResourceThen.poc")

    def testReadWithResource(self):
        self.compareResourceOMO("resource/readWithResource.poc")

    def testWriteResource(self):
        self.compareResourceOMO("resource/writeResource.poc")

    def testWriteWithResource(self):
        self.compareResourceOMO("resource/writeWithResource.poc")


