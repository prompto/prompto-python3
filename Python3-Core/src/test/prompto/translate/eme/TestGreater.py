from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestGreater(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceEME("greater/gtCharacter.pec")

    def testGtDate(self):
        self.compareResourceEME("greater/gtDate.pec")

    def testGtDateTime(self):
        self.compareResourceEME("greater/gtDateTime.pec")

    def testGtDecimal(self):
        self.compareResourceEME("greater/gtDecimal.pec")

    def testGteCharacter(self):
        self.compareResourceEME("greater/gteCharacter.pec")

    def testGteDate(self):
        self.compareResourceEME("greater/gteDate.pec")

    def testGteDateTime(self):
        self.compareResourceEME("greater/gteDateTime.pec")

    def testGteDecimal(self):
        self.compareResourceEME("greater/gteDecimal.pec")

    def testGteInteger(self):
        self.compareResourceEME("greater/gteInteger.pec")

    def testGteText(self):
        self.compareResourceEME("greater/gteText.pec")

    def testGteTime(self):
        self.compareResourceEME("greater/gteTime.pec")

    def testGtInteger(self):
        self.compareResourceEME("greater/gtInteger.pec")

    def testGtText(self):
        self.compareResourceEME("greater/gtText.pec")

    def testGtTime(self):
        self.compareResourceEME("greater/gtTime.pec")


