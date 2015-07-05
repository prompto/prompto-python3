from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out
from prompto.runtime.utils.MyResource import MyResource
from prompto.error.SyntaxError import SyntaxError

class TestResource(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
        MyResource.content = "readFullyOk"

    def tearDown(self):
        Out.restore()

    def testBadRead(self):
        try:
            self.runResource("resource/badRead.pec")
            self.fail("Should raise SyntaxError")
        except SyntaxError:
            pass

    def testBadWrite(self):
        try:
            self.runResource("resource/badWrite.pec")
            self.fail("Should raise SyntaxError")
        except SyntaxError:
            pass

    def testBadResource(self):
        try:
            self.runResource("resource/badResource.pec")
        except SyntaxError:
            pass

    def testReadResource(self):
        self.checkOutput("resource/readResource.pec")

    def testWriteResource(self):
        self.checkOutput("resource/writeResource.pec")

    def testReadWithResource(self):
        self.checkOutput("resource/readWithResource.pec")

    def testWriteWithResource(self):
        self.checkOutput("resource/writeWithResource.pec")
