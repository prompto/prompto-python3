from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestGreater(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGtCharacter(self):
        self.checkOutput("greater/gtCharacter.poc")

    def testGtDate(self):
        self.checkOutput("greater/gtDate.poc")

    def testGtDateTime(self):
        self.checkOutput("greater/gtDateTime.poc")

    def testGtDecimal(self):
        self.checkOutput("greater/gtDecimal.poc")

    def testGteCharacter(self):
        self.checkOutput("greater/gteCharacter.poc")

    def testGteDate(self):
        self.checkOutput("greater/gteDate.poc")

    def testGteDateTime(self):
        self.checkOutput("greater/gteDateTime.poc")

    def testGteDecimal(self):
        self.checkOutput("greater/gteDecimal.poc")

    def testGteInteger(self):
        self.checkOutput("greater/gteInteger.poc")

    def testGteText(self):
        self.checkOutput("greater/gteText.poc")

    def testGteTime(self):
        self.checkOutput("greater/gteTime.poc")

    def testGtInteger(self):
        self.checkOutput("greater/gtInteger.poc")

    def testGtText(self):
        self.checkOutput("greater/gtText.poc")

    def testGtTime(self):
        self.checkOutput("greater/gtTime.poc")


