from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestCast(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAutoDowncast(self):
        self.checkOutput("cast/autoDowncast.o")

    def testCastChild(self):
        self.checkOutput("cast/castChild.o")

    def testIsAChild(self):
        self.checkOutput("cast/isAChild.o")

    def testIsAText(self):
        self.checkOutput("cast/isAText.o")


