from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCondition(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceESE("condition/complexIf.pec")

    def testReturnIf(self):
        self.compareResourceESE("condition/returnIf.pec")

    def testSimpleIf(self):
        self.compareResourceESE("condition/simpleIf.pec")

    def testSwitch(self):
        self.compareResourceESE("condition/switch.pec")

    def testTernary(self):
        self.compareResourceESE("condition/ternary.pec")


