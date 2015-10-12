from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestAdd(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceESE("add/addCharacter.pec")

    def testAddDate(self):
        self.compareResourceESE("add/addDate.pec")

    def testAddDateTime(self):
        self.compareResourceESE("add/addDateTime.pec")

    def testAddDecimal(self):
        self.compareResourceESE("add/addDecimal.pec")

    def testAddDict(self):
        self.compareResourceESE("add/addDict.pec")

    def testAddInteger(self):
        self.compareResourceESE("add/addInteger.pec")

    def testAddList(self):
        self.compareResourceESE("add/addList.pec")

    def testAddPeriod(self):
        self.compareResourceESE("add/addPeriod.pec")

    def testAddSet(self):
        self.compareResourceESE("add/addSet.pec")

    def testAddText(self):
        self.compareResourceESE("add/addText.pec")

    def testAddTime(self):
        self.compareResourceESE("add/addTime.pec")

    def testAddTuple(self):
        self.compareResourceESE("add/addTuple.pec")


