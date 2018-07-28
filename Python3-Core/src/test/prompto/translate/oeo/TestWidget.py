from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestWidget(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinimal(self):
        self.compareResourceOEO("widget/minimal.poc")

    def testNative(self):
        self.compareResourceOEO("widget/native.poc")

    def testWithEvent(self):
        self.compareResourceOEO("widget/withEvent.poc")


