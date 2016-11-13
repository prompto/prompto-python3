from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestAdd(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddCharacter(self):
        self.checkOutput("add/addCharacter.pec")

    def testAddDate(self):
        self.checkOutput("add/addDate.pec")

    def testAddDateTime(self):
        self.checkOutput("add/addDateTime.pec")

    def testAddDecimal(self):
        self.checkOutput("add/addDecimal.pec")

    def testAddDecimalEnum(self):
        self.checkOutput("add/addDecimalEnum.pec")

    def testAddDict(self):
        self.checkOutput("add/addDict.pec")

    def testAddInteger(self):
        self.checkOutput("add/addInteger.pec")

    def testAddIntegerEnum(self):
        self.checkOutput("add/addIntegerEnum.pec")

    def testAddList(self):
        self.checkOutput("add/addList.pec")

    def testAddPeriod(self):
        self.checkOutput("add/addPeriod.pec")

    def testAddSet(self):
        self.checkOutput("add/addSet.pec")

    def testAddTextCharacter(self):
        self.checkOutput("add/addTextCharacter.pec")

    def testAddTextDecimal(self):
        self.checkOutput("add/addTextDecimal.pec")

    def testAddTextEnum(self):
        self.checkOutput("add/addTextEnum.pec")

    def testAddTextInteger(self):
        self.checkOutput("add/addTextInteger.pec")

    def testAddTextText(self):
        self.checkOutput("add/addTextText.pec")

    def testAddTime(self):
        self.checkOutput("add/addTime.pec")

    def testAddTuple(self):
        self.checkOutput("add/addTuple.pec")


