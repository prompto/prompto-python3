from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

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


