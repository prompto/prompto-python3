from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestAdd(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddCharacter(self):
        self.checkOutput("add/addCharacter.poc")

    def testAddDate(self):
        self.checkOutput("add/addDate.poc")

    def testAddDateTime(self):
        self.checkOutput("add/addDateTime.poc")

    def testAddDecimal(self):
        self.checkOutput("add/addDecimal.poc")

    def testAddDict(self):
        self.checkOutput("add/addDict.poc")

    def testAddDocument(self):
        self.checkOutput("add/addDocument.poc")

    def testAddInteger(self):
        self.checkOutput("add/addInteger.poc")

    def testAddList(self):
        self.checkOutput("add/addList.poc")

    def testAddListDerived(self):
        self.checkOutput("add/addListDerived.poc")

    def testAddPeriod(self):
        self.checkOutput("add/addPeriod.poc")

    def testAddSet(self):
        self.checkOutput("add/addSet.poc")

    def testAddSetDerived(self):
        self.checkOutput("add/addSetDerived.poc")

    def testAddTextCharacter(self):
        self.checkOutput("add/addTextCharacter.poc")

    def testAddTextDecimal(self):
        self.checkOutput("add/addTextDecimal.poc")

    def testAddTextInteger(self):
        self.checkOutput("add/addTextInteger.poc")

    def testAddTextText(self):
        self.checkOutput("add/addTextText.poc")

    def testAddTime(self):
        self.checkOutput("add/addTime.poc")

    def testAddTuple(self):
        self.checkOutput("add/addTuple.poc")


