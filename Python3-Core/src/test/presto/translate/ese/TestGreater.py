from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestGreater(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceESE("greater/gtCharacter.pec")

    def testGtDate(self):
        self.compareResourceESE("greater/gtDate.pec")

    def testGtDateTime(self):
        self.compareResourceESE("greater/gtDateTime.pec")

    def testGtDecimal(self):
        self.compareResourceESE("greater/gtDecimal.pec")

    def testGteCharacter(self):
        self.compareResourceESE("greater/gteCharacter.pec")

    def testGteDate(self):
        self.compareResourceESE("greater/gteDate.pec")

    def testGteDateTime(self):
        self.compareResourceESE("greater/gteDateTime.pec")

    def testGteDecimal(self):
        self.compareResourceESE("greater/gteDecimal.pec")

    def testGteInteger(self):
        self.compareResourceESE("greater/gteInteger.pec")

    def testGteText(self):
        self.compareResourceESE("greater/gteText.pec")

    def testGteTime(self):
        self.compareResourceESE("greater/gteTime.pec")

    def testGtInteger(self):
        self.compareResourceESE("greater/gtInteger.pec")

    def testGtText(self):
        self.compareResourceESE("greater/gtText.pec")

    def testGtTime(self):
        self.compareResourceESE("greater/gtTime.pec")


