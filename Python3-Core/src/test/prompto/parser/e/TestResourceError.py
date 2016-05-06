from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out
from prompto.error.SyntaxError import SyntaxError

class TestResourceError(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()

    def tearDown(self):
        Out.restore()

    def testBadRead(self):
        try:
            self.runResource("resourceError/badRead.pec")
            self.fail("Should raise SyntaxError")
        except SyntaxError:
            pass

    def testBadWrite(self):
        try:
            self.runResource("resourceError/badWrite.pec")
            self.fail("Should raise SyntaxError")
        except SyntaxError:
            pass

    def testBadResource(self):
        try:
            self.runResource("resourceError/badResource.pec")
        except SyntaxError:
            pass

