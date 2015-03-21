from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out
from presto.runtime.utils.MyResource import MyResource
from presto.error.SyntaxError import SyntaxError

class TestResource(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        MyResource.content = "readFullyOk"

    def tearDown(self):
        Out.restore()

    def testBadRead(self):
        try:
            self.runResource("resource/badRead.e")
            self.fail("Should raise SyntaxError")
        except SyntaxError:
            pass

    def testBadWrite(self):
        try:
            self.runResource("resource/badWrite.e")
            self.fail("Should raise SyntaxError")
        except SyntaxError:
            pass

    def testBadResource(self):
        try:
            self.runResource("resource/badResource.e")
        except SyntaxError:
            pass

    def testReadResource(self):
        self.checkOutput("resource/readResource.e")

    def testWriteResource(self):
        self.checkOutput("resource/writeResource.e")

    def testReadWithResource(self):
        self.checkOutput("resource/readWithResource.e")

    def testWriteWithResource(self):
        self.checkOutput("resource/writeWithResource.e")
