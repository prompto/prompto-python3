from prompto.parser.m.BaseMParserTest import BaseMParserTest
from prompto.runtime.utils.Out import Out

class TestMethods(BaseMParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testTextAsync(self):
        self.checkOutput("methods/textAsync.pmc")

    def testVoidAsync(self):
        self.checkOutput("methods/voidAsync.pmc")


