from prompto.parser.m.BaseMParserTest import BaseMParserTest
from prompto.runtime.utils.Out import Out

class TestJsx(BaseMParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testChildElement(self):
        self.checkOutput("jsx/childElement.pmc")

    def testCodeAttribute(self):
        self.checkOutput("jsx/codeAttribute.pmc")

    def testCodeElement(self):
        self.checkOutput("jsx/codeElement.pmc")

    def testDotName(self):
        self.checkOutput("jsx/dotName.pmc")

    def testEmptyAttribute(self):
        self.checkOutput("jsx/emptyAttribute.pmc")

    def testFragment(self):
        self.checkOutput("jsx/fragment.pmc")

    def testHyphenName(self):
        self.checkOutput("jsx/hyphenName.pmc")

    def testLiteralAttribute(self):
        self.checkOutput("jsx/literalAttribute.pmc")

    def testNonAsciiTextElement(self):
        self.checkOutput("jsx/nonAsciiTextElement.pmc")

    def testSelfClosingDiv(self):
        self.checkOutput("jsx/selfClosingDiv.pmc")

    def testSelfClosingEmptyAttribute(self):
        self.checkOutput("jsx/selfClosingEmptyAttribute.pmc")

    def testTextElement(self):
        self.checkOutput("jsx/textElement.pmc")


