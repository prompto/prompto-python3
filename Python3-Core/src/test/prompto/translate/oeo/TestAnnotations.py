from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAnnotations(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testWidgetField(self):
        self.compareResourceOEO("annotations/WidgetField.poc")

    def testCallback(self):
        self.compareResourceOEO("annotations/callback.poc")

    def testCategory(self):
        self.compareResourceOEO("annotations/category.poc")


