from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestResource(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testReadInDoWhile(self):
        self.checkOutput("resource/readInDoWhile.poc")

    def testReadInForEach(self):
        self.checkOutput("resource/readInForEach.poc")

    def testReadInIf(self):
        self.checkOutput("resource/readInIf.poc")

    def testReadInWhile(self):
        self.checkOutput("resource/readInWhile.poc")

    def testReadResource(self):
        self.checkOutput("resource/readResource.poc")

    def testReadResourceThen(self):
        self.checkOutput("resource/readResourceThen.poc")

    def testReadWithResource(self):
        self.checkOutput("resource/readWithResource.poc")

    def testWriteResource(self):
        self.checkOutput("resource/writeResource.poc")

    def testWriteResourceThen(self):
        self.checkOutput("resource/writeResourceThen.poc")

    def testWriteWithResource(self):
        self.checkOutput("resource/writeWithResource.poc")


