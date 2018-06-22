from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestJsx(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testChildElement(self):
        self.compareResourceOEO("jsx/childElement.poc")

    def testCodeAttribute(self):
        self.compareResourceOEO("jsx/codeAttribute.poc")

    def testCodeElement(self):
        self.compareResourceOEO("jsx/codeElement.poc")

    def testDotName(self):
        self.compareResourceOEO("jsx/dotName.poc")

    def testEmpty(self):
        self.compareResourceOEO("jsx/empty.poc")

    def testEmptyAttribute(self):
        self.compareResourceOEO("jsx/emptyAttribute.poc")

    def testHyphenName(self):
        self.compareResourceOEO("jsx/hyphenName.poc")

    def testLiteralAttribute(self):
        self.compareResourceOEO("jsx/literalAttribute.poc")

    def testSelfClosingDiv(self):
        self.compareResourceOEO("jsx/selfClosingDiv.poc")

    def testSelfClosingEmptyAttribute(self):
        self.compareResourceOEO("jsx/selfClosingEmptyAttribute.poc")

    def testTextElement(self):
        self.compareResourceOEO("jsx/textElement.poc")


