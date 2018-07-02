from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCss(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCodeValue(self):
        self.compareResourceOMO("css/codeValue.poc")

    def testHyphenName(self):
        self.compareResourceOMO("css/hyphenName.poc")

    def testMultiValue(self):
        self.compareResourceOMO("css/multiValue.poc")

    def testNumberValue(self):
        self.compareResourceOMO("css/numberValue.poc")

    def testPixelValue(self):
        self.compareResourceOMO("css/pixelValue.poc")

    def testTextValue(self):
        self.compareResourceOMO("css/textValue.poc")


