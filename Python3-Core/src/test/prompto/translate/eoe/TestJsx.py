from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestJsx(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testChildElement(self):
        self.compareResourceEOE("jsx/childElement.pec")

    def testCodeAttribute(self):
        self.compareResourceEOE("jsx/codeAttribute.pec")

    def testCodeElement(self):
        self.compareResourceEOE("jsx/codeElement.pec")

    def testDotName(self):
        self.compareResourceEOE("jsx/dotName.pec")

    def testEmpty(self):
        self.compareResourceEOE("jsx/empty.pec")

    def testEmptyAttribute(self):
        self.compareResourceEOE("jsx/emptyAttribute.pec")

    def testFragment(self):
        self.compareResourceEOE("jsx/fragment.pec")

    def testHyphenName(self):
        self.compareResourceEOE("jsx/hyphenName.pec")

    def testLiteralAttribute(self):
        self.compareResourceEOE("jsx/literalAttribute.pec")

    def testNonAsciiTextElement(self):
        self.compareResourceEOE("jsx/nonAsciiTextElement.pec")

    def testSelfClosingDiv(self):
        self.compareResourceEOE("jsx/selfClosingDiv.pec")

    def testSelfClosingEmptyAttribute(self):
        self.compareResourceEOE("jsx/selfClosingEmptyAttribute.pec")

    def testTextElement(self):
        self.compareResourceEOE("jsx/textElement.pec")


