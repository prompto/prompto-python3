from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReadResource(self):
        self.compareResourceOSO("resource/readResource.poc")

    def testReadWithResource(self):
        self.compareResourceOSO("resource/readWithResource.poc")

    def testWriteResource(self):
        self.compareResourceOSO("resource/writeResource.poc")

    def testWriteWithResource(self):
        self.compareResourceOSO("resource/writeWithResource.poc")


