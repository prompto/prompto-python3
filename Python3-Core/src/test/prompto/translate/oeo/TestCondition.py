from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceOEO("condition/complexIf.poc")

    def testElseIf(self):
        self.compareResourceOEO("condition/elseIf.poc")

    def testReturnIf(self):
        self.compareResourceOEO("condition/returnIf.poc")

    def testSimpleIf(self):
        self.compareResourceOEO("condition/simpleIf.poc")

    def testSwitch(self):
        self.compareResourceOEO("condition/switch.poc")

    def testTernary(self):
        self.compareResourceOEO("condition/ternary.poc")


