from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestGreater(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testGtCharacter(self):
        self.compareResourceOPO("greater/gtCharacter.o")

    def testGtDate(self):
        self.compareResourceOPO("greater/gtDate.o")

    def testGtDateTime(self):
        self.compareResourceOPO("greater/gtDateTime.o")

    def testGtDecimal(self):
        self.compareResourceOPO("greater/gtDecimal.o")

    def testGteCharacter(self):
        self.compareResourceOPO("greater/gteCharacter.o")

    def testGteDate(self):
        self.compareResourceOPO("greater/gteDate.o")

    def testGteDateTime(self):
        self.compareResourceOPO("greater/gteDateTime.o")

    def testGteDecimal(self):
        self.compareResourceOPO("greater/gteDecimal.o")

    def testGteInteger(self):
        self.compareResourceOPO("greater/gteInteger.o")

    def testGteText(self):
        self.compareResourceOPO("greater/gteText.o")

    def testGteTime(self):
        self.compareResourceOPO("greater/gteTime.o")

    def testGtInteger(self):
        self.compareResourceOPO("greater/gtInteger.o")

    def testGtText(self):
        self.compareResourceOPO("greater/gtText.o")

    def testGtTime(self):
        self.compareResourceOPO("greater/gtTime.o")


