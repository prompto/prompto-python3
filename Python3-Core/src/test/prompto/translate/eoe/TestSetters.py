# generated: 2015-07-05T23:01:01.930
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSetters(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceEOE("setters/getter.pec")

    def testGetterCall(self):
        self.compareResourceEOE("setters/getterCall.pec")

    def testSetter(self):
        self.compareResourceEOE("setters/setter.pec")


