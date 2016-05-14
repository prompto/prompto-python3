from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testComplexIf(self):
        self.checkOutput("condition/complexIf.poc")

    def testEmbeddedIf(self):
        self.checkOutput("condition/embeddedIf.poc")

    def testReturnIf(self):
        self.checkOutput("condition/returnIf.poc")

    def testSimpleIf(self):
        self.checkOutput("condition/simpleIf.poc")

    def testSwitch(self):
        self.checkOutput("condition/switch.poc")

    def testTernary(self):
        self.checkOutput("condition/ternary.poc")


