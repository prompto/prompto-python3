from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestLogic(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAndBoolean(self):
        self.checkOutput("logic/andBoolean.poc")

    def testNotBoolean(self):
        self.checkOutput("logic/notBoolean.poc")

    def testOrBoolean(self):
        self.checkOutput("logic/orBoolean.poc")


