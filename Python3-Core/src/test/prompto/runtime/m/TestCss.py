from prompto.parser.m.BaseMParserTest import BaseMParserTest
from prompto.runtime.utils.Out import Out

class TestCss(BaseMParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCodeValue(self):
        self.checkOutput("css/codeValue.pmc")

    def testCompositeValue(self):
        self.checkOutput("css/compositeValue.pmc")

    def testHyphenName(self):
        self.checkOutput("css/hyphenName.pmc")

    def testMultiValue(self):
        self.checkOutput("css/multiValue.pmc")

    def testNumberValue(self):
        self.checkOutput("css/numberValue.pmc")

    def testPixelValue(self):
        self.checkOutput("css/pixelValue.pmc")

    def testTextValue(self):
        self.checkOutput("css/textValue.pmc")


