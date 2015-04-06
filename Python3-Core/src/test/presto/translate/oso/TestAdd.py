from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestAdd(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceOSO("add/addCharacter.poc")

    def testAddDate(self):
        self.compareResourceOSO("add/addDate.poc")

    def testAddDateTime(self):
        self.compareResourceOSO("add/addDateTime.poc")

    def testAddDecimal(self):
        self.compareResourceOSO("add/addDecimal.poc")

    def testAddDict(self):
        self.compareResourceOSO("add/addDict.poc")

    def testAddInteger(self):
        self.compareResourceOSO("add/addInteger.poc")

    def testAddList(self):
        self.compareResourceOSO("add/addList.poc")

    def testAddPeriod(self):
        self.compareResourceOSO("add/addPeriod.poc")

    def testAddSet(self):
        self.compareResourceOSO("add/addSet.poc")

    def testAddText(self):
        self.compareResourceOSO("add/addText.poc")

    def testAddTime(self):
        self.compareResourceOSO("add/addTime.poc")

    def testAddTuple(self):
        self.compareResourceOSO("add/addTuple.poc")


