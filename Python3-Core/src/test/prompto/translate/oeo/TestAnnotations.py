from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAnnotations(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReactWidgetProps1(self):
        self.compareResourceOEO("annotations/ReactWidgetProps1.poc")

    def testReactWidgetProps2(self):
        self.compareResourceOEO("annotations/ReactWidgetProps2.poc")

    def testWidgetChildProps1(self):
        self.compareResourceOEO("annotations/WidgetChildProps1.poc")

    def testWidgetChildProps2(self):
        self.compareResourceOEO("annotations/WidgetChildProps2.poc")

    def testWidgetField(self):
        self.compareResourceOEO("annotations/WidgetField.poc")

    def testWidgetProps1(self):
        self.compareResourceOEO("annotations/WidgetProps1.poc")

    def testWidgetProps2(self):
        self.compareResourceOEO("annotations/WidgetProps2.poc")

    def testWidgetProps3(self):
        self.compareResourceOEO("annotations/WidgetProps3.poc")

    def testWidgetProps4(self):
        self.compareResourceOEO("annotations/WidgetProps4.poc")

    def testCallback(self):
        self.compareResourceOEO("annotations/callback.poc")

    def testCategory(self):
        self.compareResourceOEO("annotations/category.poc")


