from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceOMO("condition/complexIf.poc")

    def testEmbeddedIf(self):
        self.compareResourceOMO("condition/embeddedIf.poc")

    def testLocalScope(self):
        self.compareResourceOMO("condition/localScope.poc")

    def testReturnIf(self):
        self.compareResourceOMO("condition/returnIf.poc")

    def testSimpleIf(self):
        self.compareResourceOMO("condition/simpleIf.poc")

    def testSwitch(self):
        self.compareResourceOMO("condition/switch.poc")

    def testTernary(self):
        self.compareResourceOMO("condition/ternary.poc")

    def testTernaryType(self):
        self.compareResourceOMO("condition/ternaryType.poc")


