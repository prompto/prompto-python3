from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestGreater(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testGtCharacter(self):
        self.checkOutput("greater/gtCharacter.e")

    def testGtDate(self):
        self.checkOutput("greater/gtDate.e")

    def testGtDateTime(self):
        self.checkOutput("greater/gtDateTime.e")

    def testGtDecimal(self):
        self.checkOutput("greater/gtDecimal.e")

    def testGteCharacter(self):
        self.checkOutput("greater/gteCharacter.e")

    def testGteDate(self):
        self.checkOutput("greater/gteDate.e")

    def testGteDateTime(self):
        self.checkOutput("greater/gteDateTime.e")

    def testGteDecimal(self):
        self.checkOutput("greater/gteDecimal.e")

    def testGteInteger(self):
        self.checkOutput("greater/gteInteger.e")

    def testGteText(self):
        self.checkOutput("greater/gteText.e")

    def testGteTime(self):
        self.checkOutput("greater/gteTime.e")

    def testGtInteger(self):
        self.checkOutput("greater/gtInteger.e")

    def testGtText(self):
        self.checkOutput("greater/gtText.e")

    def testGtTime(self):
        self.checkOutput("greater/gtTime.e")


