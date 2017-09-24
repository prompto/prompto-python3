from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestGreater(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceOMO("greater/gtCharacter.poc")

    def testGtDate(self):
        self.compareResourceOMO("greater/gtDate.poc")

    def testGtDateTime(self):
        self.compareResourceOMO("greater/gtDateTime.poc")

    def testGtDecimal(self):
        self.compareResourceOMO("greater/gtDecimal.poc")

    def testGteCharacter(self):
        self.compareResourceOMO("greater/gteCharacter.poc")

    def testGteDate(self):
        self.compareResourceOMO("greater/gteDate.poc")

    def testGteDateTime(self):
        self.compareResourceOMO("greater/gteDateTime.poc")

    def testGteDecimal(self):
        self.compareResourceOMO("greater/gteDecimal.poc")

    def testGteInteger(self):
        self.compareResourceOMO("greater/gteInteger.poc")

    def testGteText(self):
        self.compareResourceOMO("greater/gteText.poc")

    def testGteTime(self):
        self.compareResourceOMO("greater/gteTime.poc")

    def testGtInteger(self):
        self.compareResourceOMO("greater/gtInteger.poc")

    def testGtText(self):
        self.compareResourceOMO("greater/gtText.poc")

    def testGtTime(self):
        self.compareResourceOMO("greater/gtTime.poc")

    def testGtVersion(self):
        self.compareResourceOMO("greater/gtVersion.poc")


