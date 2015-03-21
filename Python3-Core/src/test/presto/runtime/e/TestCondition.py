from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestCondition(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testComplexIf(self):
        self.checkOutput("condition/complexIf.e")

    def testElseIf(self):
        self.checkOutput("condition/elseIf.e")

    def testReturnIf(self):
        self.checkOutput("condition/returnIf.e")

    def testSimpleIf(self):
        self.checkOutput("condition/simpleIf.e")

    def testSwitch(self):
        self.checkOutput("condition/switch.e")

    def testTernary(self):
        self.checkOutput("condition/ternary.e")


