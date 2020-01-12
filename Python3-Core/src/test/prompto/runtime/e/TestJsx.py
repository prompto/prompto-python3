from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestJsx(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testChildElement(self):
        self.checkOutput("jsx/childElement.pec")

    def testCodeAttribute(self):
        self.checkOutput("jsx/codeAttribute.pec")

    def testCodeElement(self):
        self.checkOutput("jsx/codeElement.pec")

    def testDotName(self):
        self.checkOutput("jsx/dotName.pec")

    def testEmptyAttribute(self):
        self.checkOutput("jsx/emptyAttribute.pec")

    def testFragment(self):
        self.checkOutput("jsx/fragment.pec")

    def testHyphenName(self):
        self.checkOutput("jsx/hyphenName.pec")

    def testLiteralAttribute(self):
        self.checkOutput("jsx/literalAttribute.pec")

    def testSelfClosingDiv(self):
        self.checkOutput("jsx/selfClosingDiv.pec")

    def testSelfClosingEmptyAttribute(self):
        self.checkOutput("jsx/selfClosingEmptyAttribute.pec")

    def testTextElement(self):
        self.checkOutput("jsx/textElement.pec")


