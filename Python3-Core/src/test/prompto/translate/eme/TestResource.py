from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestResource(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReadResource(self):
        self.compareResourceEME("resource/readResource.pec")

    def testReadResourceThen(self):
        self.compareResourceEME("resource/readResourceThen.pec")

    def testReadWithResource(self):
        self.compareResourceEME("resource/readWithResource.pec")

    def testWriteResource(self):
        self.compareResourceEME("resource/writeResource.pec")

    def testWriteWithResource(self):
        self.compareResourceEME("resource/writeWithResource.pec")


