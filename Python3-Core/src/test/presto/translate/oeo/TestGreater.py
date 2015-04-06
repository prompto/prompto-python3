from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestGreater(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceOEO("greater/gtCharacter.poc")

    def testGtDate(self):
        self.compareResourceOEO("greater/gtDate.poc")

    def testGtDateTime(self):
        self.compareResourceOEO("greater/gtDateTime.poc")

    def testGtDecimal(self):
        self.compareResourceOEO("greater/gtDecimal.poc")

    def testGteCharacter(self):
        self.compareResourceOEO("greater/gteCharacter.poc")

    def testGteDate(self):
        self.compareResourceOEO("greater/gteDate.poc")

    def testGteDateTime(self):
        self.compareResourceOEO("greater/gteDateTime.poc")

    def testGteDecimal(self):
        self.compareResourceOEO("greater/gteDecimal.poc")

    def testGteInteger(self):
        self.compareResourceOEO("greater/gteInteger.poc")

    def testGteText(self):
        self.compareResourceOEO("greater/gteText.poc")

    def testGteTime(self):
        self.compareResourceOEO("greater/gteTime.poc")

    def testGtInteger(self):
        self.compareResourceOEO("greater/gtInteger.poc")

    def testGtText(self):
        self.compareResourceOEO("greater/gtText.poc")

    def testGtTime(self):
        self.compareResourceOEO("greater/gtTime.poc")


