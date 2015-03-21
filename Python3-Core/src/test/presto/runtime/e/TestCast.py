from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestCast(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAutoDowncast(self):
        self.checkOutput("cast/autoDowncast.e")

    def testCastChild(self):
        self.checkOutput("cast/castChild.e")

    def testIsAChild(self):
        self.checkOutput("cast/isAChild.e")

    def testIsAText(self):
        self.checkOutput("cast/isAText.e")


