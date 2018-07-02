from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCss(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCodeValue(self):
        self.compareResourceEME("css/codeValue.pec")

    def testHyphenName(self):
        self.compareResourceEME("css/hyphenName.pec")

    def testMultiValue(self):
        self.compareResourceEME("css/multiValue.pec")

    def testNumberValue(self):
        self.compareResourceEME("css/numberValue.pec")

    def testPixelValue(self):
        self.compareResourceEME("css/pixelValue.pec")

    def testTextValue(self):
        self.compareResourceEME("css/textValue.pec")


