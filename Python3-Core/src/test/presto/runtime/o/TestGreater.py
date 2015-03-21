from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestGreater(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGtCharacter(self):
        self.checkOutput("greater/gtCharacter.o")

    def testGtDate(self):
        self.checkOutput("greater/gtDate.o")

    def testGtDateTime(self):
        self.checkOutput("greater/gtDateTime.o")

    def testGtDecimal(self):
        self.checkOutput("greater/gtDecimal.o")

    def testGteCharacter(self):
        self.checkOutput("greater/gteCharacter.o")

    def testGteDate(self):
        self.checkOutput("greater/gteDate.o")

    def testGteDateTime(self):
        self.checkOutput("greater/gteDateTime.o")

    def testGteDecimal(self):
        self.checkOutput("greater/gteDecimal.o")

    def testGteInteger(self):
        self.checkOutput("greater/gteInteger.o")

    def testGteText(self):
        self.checkOutput("greater/gteText.o")

    def testGteTime(self):
        self.checkOutput("greater/gteTime.o")

    def testGtInteger(self):
        self.checkOutput("greater/gtInteger.o")

    def testGtText(self):
        self.checkOutput("greater/gtText.o")

    def testGtTime(self):
        self.checkOutput("greater/gtTime.o")


