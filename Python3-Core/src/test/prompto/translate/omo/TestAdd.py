from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAdd(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceOMO("add/addCharacter.poc")

    def testAddDate(self):
        self.compareResourceOMO("add/addDate.poc")

    def testAddDateTime(self):
        self.compareResourceOMO("add/addDateTime.poc")

    def testAddDecimal(self):
        self.compareResourceOMO("add/addDecimal.poc")

    def testAddDict(self):
        self.compareResourceOMO("add/addDict.poc")

    def testAddInteger(self):
        self.compareResourceOMO("add/addInteger.poc")

    def testAddList(self):
        self.compareResourceOMO("add/addList.poc")

    def testAddPeriod(self):
        self.compareResourceOMO("add/addPeriod.poc")

    def testAddSet(self):
        self.compareResourceOMO("add/addSet.poc")

    def testAddTextCharacter(self):
        self.compareResourceOMO("add/addTextCharacter.poc")

    def testAddTextDecimal(self):
        self.compareResourceOMO("add/addTextDecimal.poc")

    def testAddTextInteger(self):
        self.compareResourceOMO("add/addTextInteger.poc")

    def testAddTextText(self):
        self.compareResourceOMO("add/addTextText.poc")

    def testAddTime(self):
        self.compareResourceOMO("add/addTime.poc")

    def testAddTuple(self):
        self.compareResourceOMO("add/addTuple.poc")


