from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestCss(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCodeValue(self):
        self.checkOutput("css/codeValue.pec")

    def testCompositeValue(self):
        self.checkOutput("css/compositeValue.pec")

    def testHyphenName(self):
        self.checkOutput("css/hyphenName.pec")

    def testMultiValue(self):
        self.checkOutput("css/multiValue.pec")

    def testNumberValue(self):
        self.checkOutput("css/numberValue.pec")

    def testPixelValue(self):
        self.checkOutput("css/pixelValue.pec")

    def testTextValue(self):
        self.checkOutput("css/textValue.pec")


