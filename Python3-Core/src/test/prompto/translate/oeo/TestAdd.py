from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAdd(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceOEO("add/addCharacter.poc")

    def testAddDate(self):
        self.compareResourceOEO("add/addDate.poc")

    def testAddDateTime(self):
        self.compareResourceOEO("add/addDateTime.poc")

    def testAddDecimal(self):
        self.compareResourceOEO("add/addDecimal.poc")

    def testAddDict(self):
        self.compareResourceOEO("add/addDict.poc")

    def testAddInteger(self):
        self.compareResourceOEO("add/addInteger.poc")

    def testAddList(self):
        self.compareResourceOEO("add/addList.poc")

    def testAddPeriod(self):
        self.compareResourceOEO("add/addPeriod.poc")

    def testAddSet(self):
        self.compareResourceOEO("add/addSet.poc")

    def testAddText(self):
        self.compareResourceOEO("add/addText.poc")

    def testAddTime(self):
        self.compareResourceOEO("add/addTime.poc")

    def testAddTuple(self):
        self.compareResourceOEO("add/addTuple.poc")


