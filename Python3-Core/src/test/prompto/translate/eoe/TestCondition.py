from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCondition(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceEOE("condition/complexIf.pec")

    def testElseIf(self):
        self.compareResourceEOE("condition/elseIf.pec")

    def testReturnIf(self):
        self.compareResourceEOE("condition/returnIf.pec")

    def testSimpleIf(self):
        self.compareResourceEOE("condition/simpleIf.pec")

    def testSwitch(self):
        self.compareResourceEOE("condition/switch.pec")

    def testTernary(self):
        self.compareResourceEOE("condition/ternary.pec")


