from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestLogic(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAndBoolean(self):
        self.checkOutput("logic/andBoolean.o")

    def testNotBoolean(self):
        self.checkOutput("logic/notBoolean.o")

    def testOrBoolean(self):
        self.checkOutput("logic/orBoolean.o")


