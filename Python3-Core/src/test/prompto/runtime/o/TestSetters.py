from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestSetters(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGetter(self):
        self.checkOutput("setters/getter.poc")

    def testSetter(self):
        self.checkOutput("setters/setter.poc")


