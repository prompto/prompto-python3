from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceOEO("condition/complexIf.poc")

    def testEmbeddedIf(self):
        self.compareResourceOEO("condition/embeddedIf.poc")

    def testLocalScope(self):
        self.compareResourceOEO("condition/localScope.poc")

    def testReturnTextIf(self):
        self.compareResourceOEO("condition/returnTextIf.poc")

    def testReturnVoidIf(self):
        self.compareResourceOEO("condition/returnVoidIf.poc")

    def testSimpleIf(self):
        self.compareResourceOEO("condition/simpleIf.poc")

    def testSwitch(self):
        self.compareResourceOEO("condition/switch.poc")

    def testTernary(self):
        self.compareResourceOEO("condition/ternary.poc")

    def testTernaryType(self):
        self.compareResourceOEO("condition/ternaryType.poc")


