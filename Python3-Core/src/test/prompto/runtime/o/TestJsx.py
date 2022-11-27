from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestJsx(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testChildElement(self):
        self.checkOutput("jsx/childElement.poc")

    def testCodeAttribute(self):
        self.checkOutput("jsx/codeAttribute.poc")

    def testCodeElement(self):
        self.checkOutput("jsx/codeElement.poc")

    def testDotName(self):
        self.checkOutput("jsx/dotName.poc")

    def testEmptyAttribute(self):
        self.checkOutput("jsx/emptyAttribute.poc")

    def testFragment(self):
        self.checkOutput("jsx/fragment.poc")

    def testHyphenName(self):
        self.checkOutput("jsx/hyphenName.poc")

    def testLiteralAttribute(self):
        self.checkOutput("jsx/literalAttribute.poc")

    def testMethodCall(self):
        self.checkOutput("jsx/methodCall.poc")

    def testMethodRef(self):
        self.checkOutput("jsx/methodRef.poc")

    def testNonAsciiTextElement(self):
        self.checkOutput("jsx/nonAsciiTextElement.poc")

    def testSelfClosingDiv(self):
        self.checkOutput("jsx/selfClosingDiv.poc")

    def testSelfClosingEmptyAttribute(self):
        self.checkOutput("jsx/selfClosingEmptyAttribute.poc")

    def testTextElement(self):
        self.checkOutput("jsx/textElement.poc")

    def testThisLowerMethodRef(self):
        self.checkOutput("jsx/thisLowerMethodRef.poc")

    def testThisMethodCall(self):
        self.checkOutput("jsx/thisMethodCall.poc")

    def testThisUpperMethodRef(self):
        self.checkOutput("jsx/thisUpperMethodRef.poc")


