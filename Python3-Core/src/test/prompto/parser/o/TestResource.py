from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out
from prompto.runtime.utils.MyResource import MyResource
from prompto.error.SyntaxError import SyntaxError


class TestResource(BaseOParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        MyResource.content = "readFullyOk"

    def tearDown(self):
        Out.restore()

    def testBadRead(self):
        try:
            self.runResource("resource/badRead.poc")
            self.fail()
        except SyntaxError:
            pass

    def testBadWrite(self):
        try:
            self.runResource("resource/badWrite.poc")
            self.fail()
        except SyntaxError:
            pass

    def testBadResource(self):
        try:
            self.runResource("resource/badResource.poc")
            self.fail()
        except SyntaxError:
            pass


    def testReadResource(self):
        self.checkOutput("resource/readResource.poc")


    def testWriteResource(self):
        self.checkOutput("resource/writeResource.poc")


    def testReadWithResource(self):
        self.checkOutput("resource/readWithResource.poc")


    def testWriteWithResource(self):
        self.checkOutput("resource/writeWithResource.poc")
