from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestGreater(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceEOE("greater/gtCharacter.pec")

    def testGtDate(self):
        self.compareResourceEOE("greater/gtDate.pec")

    def testGtDateTime(self):
        self.compareResourceEOE("greater/gtDateTime.pec")

    def testGtDecimal(self):
        self.compareResourceEOE("greater/gtDecimal.pec")

    def testGteCharacter(self):
        self.compareResourceEOE("greater/gteCharacter.pec")

    def testGteDate(self):
        self.compareResourceEOE("greater/gteDate.pec")

    def testGteDateTime(self):
        self.compareResourceEOE("greater/gteDateTime.pec")

    def testGteDecimal(self):
        self.compareResourceEOE("greater/gteDecimal.pec")

    def testGteInteger(self):
        self.compareResourceEOE("greater/gteInteger.pec")

    def testGteText(self):
        self.compareResourceEOE("greater/gteText.pec")

    def testGteTime(self):
        self.compareResourceEOE("greater/gteTime.pec")

    def testGtInteger(self):
        self.compareResourceEOE("greater/gtInteger.pec")

    def testGtText(self):
        self.compareResourceEOE("greater/gtText.pec")

    def testGtTime(self):
        self.compareResourceEOE("greater/gtTime.pec")

    def testGtVersion(self):
        self.compareResourceEOE("greater/gtVersion.pec")


