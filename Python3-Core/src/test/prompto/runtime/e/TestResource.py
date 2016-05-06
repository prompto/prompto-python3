from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestResource(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testReadResource(self):
        self.checkOutput("resource/readResource.pec")

    def testReadWithResource(self):
        self.checkOutput("resource/readWithResource.pec")

    def testWriteResource(self):
        self.checkOutput("resource/writeResource.pec")

    def testWriteWithResource(self):
        self.checkOutput("resource/writeWithResource.pec")


