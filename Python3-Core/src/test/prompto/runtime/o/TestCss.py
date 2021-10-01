from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestCss(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCodeValue(self):
        self.checkOutput("css/codeValue.poc")

    def testCompositeValue(self):
        self.checkOutput("css/compositeValue.poc")

    def testHyphenName(self):
        self.checkOutput("css/hyphenName.poc")

    def testMultiValue(self):
        self.checkOutput("css/multiValue.poc")

    def testNumberValue(self):
        self.checkOutput("css/numberValue.poc")

    def testPixelValue(self):
        self.checkOutput("css/pixelValue.poc")

    def testTextValue(self):
        self.checkOutput("css/textValue.poc")


