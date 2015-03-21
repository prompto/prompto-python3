from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestGreater(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceEPE("greater/gtCharacter.e")

    def testGtDate(self):
        self.compareResourceEPE("greater/gtDate.e")

    def testGtDateTime(self):
        self.compareResourceEPE("greater/gtDateTime.e")

    def testGtDecimal(self):
        self.compareResourceEPE("greater/gtDecimal.e")

    def testGteCharacter(self):
        self.compareResourceEPE("greater/gteCharacter.e")

    def testGteDate(self):
        self.compareResourceEPE("greater/gteDate.e")

    def testGteDateTime(self):
        self.compareResourceEPE("greater/gteDateTime.e")

    def testGteDecimal(self):
        self.compareResourceEPE("greater/gteDecimal.e")

    def testGteInteger(self):
        self.compareResourceEPE("greater/gteInteger.e")

    def testGteText(self):
        self.compareResourceEPE("greater/gteText.e")

    def testGteTime(self):
        self.compareResourceEPE("greater/gteTime.e")

    def testGtInteger(self):
        self.compareResourceEPE("greater/gtInteger.e")

    def testGtText(self):
        self.compareResourceEPE("greater/gtText.e")

    def testGtTime(self):
        self.compareResourceEPE("greater/gtTime.e")


