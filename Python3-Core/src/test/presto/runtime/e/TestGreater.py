from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestGreater(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGtCharacter(self):
        self.checkOutput("greater/gtCharacter.pec")

    def testGtDate(self):
        self.checkOutput("greater/gtDate.pec")

    def testGtDateTime(self):
        self.checkOutput("greater/gtDateTime.pec")

    def testGtDecimal(self):
        self.checkOutput("greater/gtDecimal.pec")

    def testGteCharacter(self):
        self.checkOutput("greater/gteCharacter.pec")

    def testGteDate(self):
        self.checkOutput("greater/gteDate.pec")

    def testGteDateTime(self):
        self.checkOutput("greater/gteDateTime.pec")

    def testGteDecimal(self):
        self.checkOutput("greater/gteDecimal.pec")

    def testGteInteger(self):
        self.checkOutput("greater/gteInteger.pec")

    def testGteText(self):
        self.checkOutput("greater/gteText.pec")

    def testGteTime(self):
        self.checkOutput("greater/gteTime.pec")

    def testGtInteger(self):
        self.checkOutput("greater/gtInteger.pec")

    def testGtText(self):
        self.checkOutput("greater/gtText.pec")

    def testGtTime(self):
        self.checkOutput("greater/gtTime.pec")


