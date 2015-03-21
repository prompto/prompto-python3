from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCategory(self):
        self.checkOutput("native/category.e")

    def testMethod(self):
        self.checkOutput("native/method.e")


