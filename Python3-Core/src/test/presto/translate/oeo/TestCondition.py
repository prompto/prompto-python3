from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceOEO("condition/complexIf.o")

    def testElseIf(self):
        self.compareResourceOEO("condition/elseIf.o")

    def testReturnIf(self):
        self.compareResourceOEO("condition/returnIf.o")

    def testSimpleIf(self):
        self.compareResourceOEO("condition/simpleIf.o")

    def testSwitch(self):
        self.compareResourceOEO("condition/switch.o")

    def testTernary(self):
        self.compareResourceOEO("condition/ternary.o")


