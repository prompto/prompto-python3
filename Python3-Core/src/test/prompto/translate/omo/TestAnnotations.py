from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAnnotations(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testWidgetField(self):
        self.compareResourceOMO("annotations/WidgetField.poc")

    def testCallback(self):
        self.compareResourceOMO("annotations/callback.poc")

    def testCategory(self):
        self.compareResourceOMO("annotations/category.poc")


