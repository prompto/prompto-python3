from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCss(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCodeValue(self):
        self.compareResourceOEO("css/codeValue.poc")

    def testCompositeValue(self):
        self.compareResourceOEO("css/compositeValue.poc")

    def testHyphenName(self):
        self.compareResourceOEO("css/hyphenName.poc")

    def testMultiValue(self):
        self.compareResourceOEO("css/multiValue.poc")

    def testNumberValue(self):
        self.compareResourceOEO("css/numberValue.poc")

    def testPixelValue(self):
        self.compareResourceOEO("css/pixelValue.poc")

    def testTextValue(self):
        self.compareResourceOEO("css/textValue.poc")


