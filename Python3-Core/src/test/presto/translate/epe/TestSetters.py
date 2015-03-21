from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSetters(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceEPE("setters/getter.e")

    def testSetter(self):
        self.compareResourceEPE("setters/setter.e")


