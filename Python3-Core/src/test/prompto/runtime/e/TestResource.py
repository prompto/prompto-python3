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

    def testReadResourceThen(self):
        self.checkOutput("resource/readResourceThen.pec")

    def testReadWithResource(self):
        self.checkOutput("resource/readWithResource.pec")

    def testWriteResource(self):
        self.checkOutput("resource/writeResource.pec")

    def testWriteResourceThen(self):
        self.checkOutput("resource/writeResourceThen.pec")

    def testWriteWithResource(self):
        self.checkOutput("resource/writeWithResource.pec")


