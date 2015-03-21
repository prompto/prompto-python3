from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestAdd(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceEPE("add/addCharacter.e")

    def testAddDate(self):
        self.compareResourceEPE("add/addDate.e")

    def testAddDateTime(self):
        self.compareResourceEPE("add/addDateTime.e")

    def testAddDecimal(self):
        self.compareResourceEPE("add/addDecimal.e")

    def testAddDict(self):
        self.compareResourceEPE("add/addDict.e")

    def testAddInteger(self):
        self.compareResourceEPE("add/addInteger.e")

    def testAddList(self):
        self.compareResourceEPE("add/addList.e")

    def testAddPeriod(self):
        self.compareResourceEPE("add/addPeriod.e")

    def testAddSet(self):
        self.compareResourceEPE("add/addSet.e")

    def testAddText(self):
        self.compareResourceEPE("add/addText.e")

    def testAddTime(self):
        self.compareResourceEPE("add/addTime.e")

    def testAddTuple(self):
        self.compareResourceEPE("add/addTuple.e")


