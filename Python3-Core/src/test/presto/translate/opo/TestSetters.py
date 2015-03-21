from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSetters(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceOPO("setters/getter.o")

    def testSetter(self):
        self.compareResourceOPO("setters/setter.o")


