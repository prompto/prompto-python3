from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestWidget(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinimal(self):
        self.compareResourceOMO("widget/minimal.poc")

    def testNative(self):
        self.compareResourceOMO("widget/native.poc")

    def testWithDocumentLiteral(self):
        self.compareResourceOMO("widget/withDocumentLiteral.poc")

    def testWithEvent(self):
        self.compareResourceOMO("widget/withEvent.poc")


