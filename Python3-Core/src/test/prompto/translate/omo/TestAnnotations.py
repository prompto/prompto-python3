from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAnnotations(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReactWidgetProps1(self):
        self.compareResourceOMO("annotations/ReactWidgetProps1.poc")

    def testReactWidgetProps2(self):
        self.compareResourceOMO("annotations/ReactWidgetProps2.poc")

    def testWidgetChildProps1(self):
        self.compareResourceOMO("annotations/WidgetChildProps1.poc")

    def testWidgetChildProps2(self):
        self.compareResourceOMO("annotations/WidgetChildProps2.poc")

    def testWidgetField(self):
        self.compareResourceOMO("annotations/WidgetField.poc")

    def testWidgetProps1(self):
        self.compareResourceOMO("annotations/WidgetProps1.poc")

    def testWidgetProps2(self):
        self.compareResourceOMO("annotations/WidgetProps2.poc")

    def testWidgetProps3(self):
        self.compareResourceOMO("annotations/WidgetProps3.poc")

    def testWidgetProps4(self):
        self.compareResourceOMO("annotations/WidgetProps4.poc")

    def testCallback(self):
        self.compareResourceOMO("annotations/callback.poc")

    def testCategory(self):
        self.compareResourceOMO("annotations/category.poc")


