from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestLogic(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAndBoolean(self):
        self.checkOutput("logic/andBoolean.pec")

    def testNotBoolean(self):
        self.checkOutput("logic/notBoolean.pec")

    def testOrBoolean(self):
        self.checkOutput("logic/orBoolean.pec")

    def testRightSkipped(self):
        self.checkOutput("logic/rightSkipped.pec")


