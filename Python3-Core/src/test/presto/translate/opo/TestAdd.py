from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestAdd(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceOPO("add/addCharacter.o")

    def testAddDate(self):
        self.compareResourceOPO("add/addDate.o")

    def testAddDateTime(self):
        self.compareResourceOPO("add/addDateTime.o")

    def testAddDecimal(self):
        self.compareResourceOPO("add/addDecimal.o")

    def testAddDict(self):
        self.compareResourceOPO("add/addDict.o")

    def testAddInteger(self):
        self.compareResourceOPO("add/addInteger.o")

    def testAddList(self):
        self.compareResourceOPO("add/addList.o")

    def testAddPeriod(self):
        self.compareResourceOPO("add/addPeriod.o")

    def testAddSet(self):
        self.compareResourceOPO("add/addSet.o")

    def testAddText(self):
        self.compareResourceOPO("add/addText.o")

    def testAddTime(self):
        self.compareResourceOPO("add/addTime.o")

    def testAddTuple(self):
        self.compareResourceOPO("add/addTuple.o")


