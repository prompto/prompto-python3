from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestAdd(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddCharacter(self):
        self.checkOutput("add/addCharacter.o")

    def testAddDate(self):
        self.checkOutput("add/addDate.o")

    def testAddDateTime(self):
        self.checkOutput("add/addDateTime.o")

    def testAddDecimal(self):
        self.checkOutput("add/addDecimal.o")

    def testAddDict(self):
        self.checkOutput("add/addDict.o")

    def testAddInteger(self):
        self.checkOutput("add/addInteger.o")

    def testAddList(self):
        self.checkOutput("add/addList.o")

    def testAddPeriod(self):
        self.checkOutput("add/addPeriod.o")

    def testAddSet(self):
        self.checkOutput("add/addSet.o")

    def testAddText(self):
        self.checkOutput("add/addText.o")

    def testAddTime(self):
        self.checkOutput("add/addTime.o")

    def testAddTuple(self):
        self.checkOutput("add/addTuple.o")


