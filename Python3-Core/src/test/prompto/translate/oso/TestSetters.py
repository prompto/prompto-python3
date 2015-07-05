# generated: 2015-07-05T23:01:01.935
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSetters(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGetter(self):
        self.compareResourceOSO("setters/getter.poc")

    def testSetter(self):
        self.compareResourceOSO("setters/setter.poc")


