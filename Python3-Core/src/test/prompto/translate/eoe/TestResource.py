from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestResource(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReadResource(self):
        self.compareResourceEOE("resource/readResource.pec")

    def testReadWithResource(self):
        self.compareResourceEOE("resource/readWithResource.pec")

    def testWriteResource(self):
        self.compareResourceEOE("resource/writeResource.pec")

    def testWriteWithResource(self):
        self.compareResourceEOE("resource/writeWithResource.pec")


