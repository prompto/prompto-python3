from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestAdd(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddCharacter(self):
        self.checkOutput("add/addCharacter.e")

    def testAddDate(self):
        self.checkOutput("add/addDate.e")

    def testAddDateTime(self):
        self.checkOutput("add/addDateTime.e")

    def testAddDecimal(self):
        self.checkOutput("add/addDecimal.e")

    def testAddDict(self):
        self.checkOutput("add/addDict.e")

    def testAddInteger(self):
        self.checkOutput("add/addInteger.e")

    def testAddList(self):
        self.checkOutput("add/addList.e")

    def testAddPeriod(self):
        self.checkOutput("add/addPeriod.e")

    def testAddSet(self):
        self.checkOutput("add/addSet.e")

    def testAddText(self):
        self.checkOutput("add/addText.e")

    def testAddTime(self):
        self.checkOutput("add/addTime.e")

    def testAddTuple(self):
        self.checkOutput("add/addTuple.e")


