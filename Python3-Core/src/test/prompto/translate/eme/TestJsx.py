from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestJsx(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testChildElement(self):
        self.compareResourceEME("jsx/childElement.pec")

    def testCodeAttribute(self):
        self.compareResourceEME("jsx/codeAttribute.pec")

    def testCodeElement(self):
        self.compareResourceEME("jsx/codeElement.pec")

    def testDotName(self):
        self.compareResourceEME("jsx/dotName.pec")

    def testEmpty(self):
        self.compareResourceEME("jsx/empty.pec")

    def testEmptyAttribute(self):
        self.compareResourceEME("jsx/emptyAttribute.pec")

    def testFragment(self):
        self.compareResourceEME("jsx/fragment.pec")

    def testHyphenName(self):
        self.compareResourceEME("jsx/hyphenName.pec")

    def testLiteralAttribute(self):
        self.compareResourceEME("jsx/literalAttribute.pec")

    def testSelfClosingDiv(self):
        self.compareResourceEME("jsx/selfClosingDiv.pec")

    def testSelfClosingEmptyAttribute(self):
        self.compareResourceEME("jsx/selfClosingEmptyAttribute.pec")

    def testTextElement(self):
        self.compareResourceEME("jsx/textElement.pec")


