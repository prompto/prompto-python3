from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestIterate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testForEachCategoryList(self):
        self.checkOutput("iterate/forEachCategoryList.pec")

    def testForEachExpression(self):
        self.checkOutput("iterate/forEachExpression.pec")

    def testForEachIntegerList(self):
        self.checkOutput("iterate/forEachIntegerList.pec")


