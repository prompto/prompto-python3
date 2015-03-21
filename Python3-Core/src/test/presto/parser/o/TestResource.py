from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out
from presto.runtime.utils.MyResource import MyResource
from presto.error.SyntaxError import SyntaxError


class TestResource(BaseOParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        MyResource.content = "readFullyOk"

    def tearDown(self):
        Out.restore()

    def testBadRead(self):
        try:
            self.runResource("resource/badRead.o")
            self.fail()
        except SyntaxError:
            pass

    def testBadWrite(self):
        try:
            self.runResource("resource/badWrite.o")
            self.fail()
        except SyntaxError:
            pass

    def testBadResource(self):
        try:
            self.runResource("resource/badResource.o")
            self.fail()
        except SyntaxError:
            pass


    def testReadResource(self):
        self.checkOutput("resource/readResource.o")


    def testWriteResource(self):
        self.checkOutput("resource/writeResource.o")


    def testReadWithResource(self):
        self.checkOutput("resource/readWithResource.o")


    def testWriteWithResource(self):
        self.checkOutput("resource/writeWithResource.o")
