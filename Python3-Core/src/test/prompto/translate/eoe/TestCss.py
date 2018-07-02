from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCss(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCodeValue(self):
        self.compareResourceEOE("css/codeValue.pec")

    def testHyphenName(self):
        self.compareResourceEOE("css/hyphenName.pec")

    def testMultiValue(self):
        self.compareResourceEOE("css/multiValue.pec")

    def testNumberValue(self):
        self.compareResourceEOE("css/numberValue.pec")

    def testPixelValue(self):
        self.compareResourceEOE("css/pixelValue.pec")

    def testTextValue(self):
        self.compareResourceEOE("css/textValue.pec")


