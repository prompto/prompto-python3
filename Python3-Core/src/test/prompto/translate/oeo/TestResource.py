from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReadResource(self):
        self.compareResourceOEO("resource/readResource.poc")

    def testReadWithResource(self):
        self.compareResourceOEO("resource/readWithResource.poc")

    def testWriteResource(self):
        self.compareResourceOEO("resource/writeResource.poc")

    def testWriteWithResource(self):
        self.compareResourceOEO("resource/writeWithResource.poc")


