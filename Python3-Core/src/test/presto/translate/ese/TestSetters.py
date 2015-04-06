from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSetters(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceESE("setters/getter.pec")

    def testSetter(self):
        self.compareResourceESE("setters/setter.pec")


