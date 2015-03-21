from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSetters(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceEOE("setters/getter.e")

    def testSetter(self):
        self.compareResourceEOE("setters/setter.e")


