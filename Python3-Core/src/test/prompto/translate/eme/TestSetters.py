from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSetters(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceEME("setters/getter.pec")

    def testGetterCall(self):
        self.compareResourceEME("setters/getterCall.pec")

    def testSetter(self):
        self.compareResourceEME("setters/setter.pec")


