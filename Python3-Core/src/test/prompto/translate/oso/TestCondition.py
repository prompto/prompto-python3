from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceOSO("condition/complexIf.poc")

    def testEmbeddedIf(self):
        self.compareResourceOSO("condition/embeddedIf.poc")

    def testReturnIf(self):
        self.compareResourceOSO("condition/returnIf.poc")

    def testSimpleIf(self):
        self.compareResourceOSO("condition/simpleIf.poc")

    def testSwitch(self):
        self.compareResourceOSO("condition/switch.poc")

    def testTernary(self):
        self.compareResourceOSO("condition/ternary.poc")


