from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestIterate(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testForEachExpression(self):
        self.checkOutput("iterate/forEachExpression.poc")

    def testForEachIntegerList(self):
        self.checkOutput("iterate/forEachIntegerList.poc")

    def testForEachIntegerRange(self):
        self.checkOutput("iterate/forEachIntegerRange.poc")


