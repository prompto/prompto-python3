from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceOPO("condition/complexIf.o")

    def testElseIf(self):
        self.compareResourceOPO("condition/elseIf.o")

    def testReturnIf(self):
        self.compareResourceOPO("condition/returnIf.o")

    def testSimpleIf(self):
        self.compareResourceOPO("condition/simpleIf.o")

    def testSwitch(self):
        self.compareResourceOPO("condition/switch.o")

    def testTernary(self):
        self.compareResourceOPO("condition/ternary.o")


