from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSetters(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceOMO("setters/getter.poc")

    def testSetter(self):
        self.compareResourceOMO("setters/setter.poc")


