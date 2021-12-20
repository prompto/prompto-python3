from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAnnotations(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testReactState1(self):
        self.compareResourceOEO("annotations/ReactState1.poc")

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

    def testWidgetProps10(self):
        self.compareResourceOEO("annotations/WidgetProps10.poc")

    def testWidgetProps11(self):
        self.compareResourceOEO("annotations/WidgetProps11.poc")

    def testWidgetProps12(self):
        self.compareResourceOEO("annotations/WidgetProps12.poc")

    def testWidgetProps13(self):
        self.compareResourceOEO("annotations/WidgetProps13.poc")

    def testWidgetProps2(self):
        self.compareResourceOEO("annotations/WidgetProps2.poc")

    def testWidgetProps3(self):
        self.compareResourceOEO("annotations/WidgetProps3.poc")

    def testWidgetProps4(self):
        self.compareResourceOEO("annotations/WidgetProps4.poc")

    def testWidgetProps5(self):
        self.compareResourceOEO("annotations/WidgetProps5.poc")

    def testWidgetProps6(self):
        self.compareResourceOEO("annotations/WidgetProps6.poc")

    def testWidgetProps7(self):
        self.compareResourceOEO("annotations/WidgetProps7.poc")

    def testWidgetProps8(self):
        self.compareResourceOEO("annotations/WidgetProps8.poc")

    def testWidgetProps9(self):
        self.compareResourceOEO("annotations/WidgetProps9.poc")

    def testCallback(self):
        self.compareResourceOEO("annotations/callback.poc")

    def testCategory(self):
        self.compareResourceOEO("annotations/category.poc")

    def testInlined(self):
        self.compareResourceOEO("annotations/inlined.poc")


