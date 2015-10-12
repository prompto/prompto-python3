from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSetters(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceOSO("setters/getter.poc")

    def testSetter(self):
        self.compareResourceOSO("setters/setter.poc")


