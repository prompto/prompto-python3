from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestCondition(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceEPE("condition/complexIf.e")

    def testElseIf(self):
        self.compareResourceEPE("condition/elseIf.e")

    def testReturnIf(self):
        self.compareResourceEPE("condition/returnIf.e")

    def testSimpleIf(self):
        self.compareResourceEPE("condition/simpleIf.e")

    def testSwitch(self):
        self.compareResourceEPE("condition/switch.e")

    def testTernary(self):
        self.compareResourceEPE("condition/ternary.e")


