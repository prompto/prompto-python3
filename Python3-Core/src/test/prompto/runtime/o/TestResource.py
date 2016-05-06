from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testReadResource(self):
        self.checkOutput("resource/readResource.poc")

    def testReadWithResource(self):
        self.checkOutput("resource/readWithResource.poc")

    def testWriteResource(self):
        self.checkOutput("resource/writeResource.poc")

    def testWriteWithResource(self):
        self.checkOutput("resource/writeWithResource.poc")


