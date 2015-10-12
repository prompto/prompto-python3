from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestGreater(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceOSO("greater/gtCharacter.poc")

    def testGtDate(self):
        self.compareResourceOSO("greater/gtDate.poc")

    def testGtDateTime(self):
        self.compareResourceOSO("greater/gtDateTime.poc")

    def testGtDecimal(self):
        self.compareResourceOSO("greater/gtDecimal.poc")

    def testGteCharacter(self):
        self.compareResourceOSO("greater/gteCharacter.poc")

    def testGteDate(self):
        self.compareResourceOSO("greater/gteDate.poc")

    def testGteDateTime(self):
        self.compareResourceOSO("greater/gteDateTime.poc")

    def testGteDecimal(self):
        self.compareResourceOSO("greater/gteDecimal.poc")

    def testGteInteger(self):
        self.compareResourceOSO("greater/gteInteger.poc")

    def testGteText(self):
        self.compareResourceOSO("greater/gteText.poc")

    def testGteTime(self):
        self.compareResourceOSO("greater/gteTime.poc")

    def testGtInteger(self):
        self.compareResourceOSO("greater/gtInteger.poc")

    def testGtText(self):
        self.compareResourceOSO("greater/gtText.poc")

    def testGtTime(self):
        self.compareResourceOSO("greater/gtTime.poc")


