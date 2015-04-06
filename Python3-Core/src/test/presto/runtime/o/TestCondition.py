from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testComplexIf(self):
        self.checkOutput("condition/complexIf.poc")

    def testElseIf(self):
        self.checkOutput("condition/elseIf.poc")

    def testReturnIf(self):
        self.checkOutput("condition/returnIf.poc")

    def testSimpleIf(self):
        self.checkOutput("condition/simpleIf.poc")

    def testSwitch(self):
        self.checkOutput("condition/switch.poc")

    def testTernary(self):
        self.checkOutput("condition/ternary.poc")


