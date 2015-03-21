from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestGreater(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceOEO("greater/gtCharacter.o")

    def testGtDate(self):
        self.compareResourceOEO("greater/gtDate.o")

    def testGtDateTime(self):
        self.compareResourceOEO("greater/gtDateTime.o")

    def testGtDecimal(self):
        self.compareResourceOEO("greater/gtDecimal.o")

    def testGteCharacter(self):
        self.compareResourceOEO("greater/gteCharacter.o")

    def testGteDate(self):
        self.compareResourceOEO("greater/gteDate.o")

    def testGteDateTime(self):
        self.compareResourceOEO("greater/gteDateTime.o")

    def testGteDecimal(self):
        self.compareResourceOEO("greater/gteDecimal.o")

    def testGteInteger(self):
        self.compareResourceOEO("greater/gteInteger.o")

    def testGteText(self):
        self.compareResourceOEO("greater/gteText.o")

    def testGteTime(self):
        self.compareResourceOEO("greater/gteTime.o")

    def testGtInteger(self):
        self.compareResourceOEO("greater/gtInteger.o")

    def testGtText(self):
        self.compareResourceOEO("greater/gtText.o")

    def testGtTime(self):
        self.compareResourceOEO("greater/gtTime.o")


