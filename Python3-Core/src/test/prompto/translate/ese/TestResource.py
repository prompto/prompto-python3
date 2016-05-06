from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestResource(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReadResource(self):
        self.compareResourceESE("resource/readResource.pec")

    def testReadWithResource(self):
        self.compareResourceESE("resource/readWithResource.pec")

    def testWriteResource(self):
        self.compareResourceESE("resource/writeResource.pec")

    def testWriteWithResource(self):
        self.compareResourceESE("resource/writeWithResource.pec")


