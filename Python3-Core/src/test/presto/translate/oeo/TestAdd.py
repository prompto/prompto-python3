from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestAdd(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceOEO("add/addCharacter.o")

    def testAddDate(self):
        self.compareResourceOEO("add/addDate.o")

    def testAddDateTime(self):
        self.compareResourceOEO("add/addDateTime.o")

    def testAddDecimal(self):
        self.compareResourceOEO("add/addDecimal.o")

    def testAddDict(self):
        self.compareResourceOEO("add/addDict.o")

    def testAddInteger(self):
        self.compareResourceOEO("add/addInteger.o")

    def testAddList(self):
        self.compareResourceOEO("add/addList.o")

    def testAddPeriod(self):
        self.compareResourceOEO("add/addPeriod.o")

    def testAddSet(self):
        self.compareResourceOEO("add/addSet.o")

    def testAddText(self):
        self.compareResourceOEO("add/addText.o")

    def testAddTime(self):
        self.compareResourceOEO("add/addTime.o")

    def testAddTuple(self):
        self.compareResourceOEO("add/addTuple.o")


