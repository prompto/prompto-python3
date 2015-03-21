from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestCondition(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceEOE("condition/complexIf.e")

    def testElseIf(self):
        self.compareResourceEOE("condition/elseIf.e")

    def testReturnIf(self):
        self.compareResourceEOE("condition/returnIf.e")

    def testSimpleIf(self):
        self.compareResourceEOE("condition/simpleIf.e")

    def testSwitch(self):
        self.compareResourceEOE("condition/switch.e")

    def testTernary(self):
        self.compareResourceEOE("condition/ternary.e")


