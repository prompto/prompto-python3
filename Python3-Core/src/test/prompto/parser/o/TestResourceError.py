from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out
from prompto.error.SyntaxError import SyntaxError


class TestResourceError(BaseOParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()

    def tearDown(self):
        Out.restore()

    def testBadRead(self):
        try:
            self.runResource("resourceError/badRead.poc")
            self.fail()
        except SyntaxError:
            pass

    def testBadWrite(self):
        try:
            self.runResource("resourceError/badWrite.poc")
            self.fail()
        except SyntaxError:
            pass

    def testBadResource(self):
        try:
            self.runResource("resourceError/badResource.poc")
            self.fail()
        except SyntaxError:
            pass


