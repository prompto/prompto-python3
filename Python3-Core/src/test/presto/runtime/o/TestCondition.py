from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testComplexIf(self):
        self.checkOutput("condition/complexIf.o")

    def testElseIf(self):
        self.checkOutput("condition/elseIf.o")

    def testReturnIf(self):
        self.checkOutput("condition/returnIf.o")

    def testSimpleIf(self):
        self.checkOutput("condition/simpleIf.o")

    def testSwitch(self):
        self.checkOutput("condition/switch.o")

    def testTernary(self):
        self.checkOutput("condition/ternary.o")


