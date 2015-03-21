from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestGreater(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceEOE("greater/gtCharacter.e")

    def testGtDate(self):
        self.compareResourceEOE("greater/gtDate.e")

    def testGtDateTime(self):
        self.compareResourceEOE("greater/gtDateTime.e")

    def testGtDecimal(self):
        self.compareResourceEOE("greater/gtDecimal.e")

    def testGteCharacter(self):
        self.compareResourceEOE("greater/gteCharacter.e")

    def testGteDate(self):
        self.compareResourceEOE("greater/gteDate.e")

    def testGteDateTime(self):
        self.compareResourceEOE("greater/gteDateTime.e")

    def testGteDecimal(self):
        self.compareResourceEOE("greater/gteDecimal.e")

    def testGteInteger(self):
        self.compareResourceEOE("greater/gteInteger.e")

    def testGteText(self):
        self.compareResourceEOE("greater/gteText.e")

    def testGteTime(self):
        self.compareResourceEOE("greater/gteTime.e")

    def testGtInteger(self):
        self.compareResourceEOE("greater/gtInteger.e")

    def testGtText(self):
        self.compareResourceEOE("greater/gtText.e")

    def testGtTime(self):
        self.compareResourceEOE("greater/gtTime.e")


