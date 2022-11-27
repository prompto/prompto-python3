from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestJsx(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testChildElement(self):
        self.compareResourceOMO("jsx/childElement.poc")

    def testCodeAttribute(self):
        self.compareResourceOMO("jsx/codeAttribute.poc")

    def testCodeElement(self):
        self.compareResourceOMO("jsx/codeElement.poc")

    def testDotName(self):
        self.compareResourceOMO("jsx/dotName.poc")

    def testEmpty(self):
        self.compareResourceOMO("jsx/empty.poc")

    def testEmptyAttribute(self):
        self.compareResourceOMO("jsx/emptyAttribute.poc")

    def testFragment(self):
        self.compareResourceOMO("jsx/fragment.poc")

    def testHyphenName(self):
        self.compareResourceOMO("jsx/hyphenName.poc")

    def testLiteralAttribute(self):
        self.compareResourceOMO("jsx/literalAttribute.poc")

    def testMethodCall(self):
        self.compareResourceOMO("jsx/methodCall.poc")

    def testMethodRef(self):
        self.compareResourceOMO("jsx/methodRef.poc")

    def testNonAsciiTextElement(self):
        self.compareResourceOMO("jsx/nonAsciiTextElement.poc")

    def testSelfClosingDiv(self):
        self.compareResourceOMO("jsx/selfClosingDiv.poc")

    def testSelfClosingEmptyAttribute(self):
        self.compareResourceOMO("jsx/selfClosingEmptyAttribute.poc")

    def testTextElement(self):
        self.compareResourceOMO("jsx/textElement.poc")

    def testThisLowerMethodRef(self):
        self.compareResourceOMO("jsx/thisLowerMethodRef.poc")

    def testThisMethodCall(self):
        self.compareResourceOMO("jsx/thisMethodCall.poc")

    def testThisUpperMethodRef(self):
        self.compareResourceOMO("jsx/thisUpperMethodRef.poc")


