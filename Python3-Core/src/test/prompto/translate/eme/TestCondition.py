from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCondition(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComplexIf(self):
        self.compareResourceEME("condition/complexIf.pec")

    def testEmbeddedIf(self):
        self.compareResourceEME("condition/embeddedIf.pec")

    def testReturnTextIf(self):
        self.compareResourceEME("condition/returnTextIf.pec")

    def testReturnVoidIf(self):
        self.compareResourceEME("condition/returnVoidIf.pec")

    def testSimpleIf(self):
        self.compareResourceEME("condition/simpleIf.pec")

    def testSwitch(self):
        self.compareResourceEME("condition/switch.pec")

    def testTernary(self):
        self.compareResourceEME("condition/ternary.pec")


