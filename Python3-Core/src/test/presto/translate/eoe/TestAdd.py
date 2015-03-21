from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestAdd(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceEOE("add/addCharacter.e")

    def testAddDate(self):
        self.compareResourceEOE("add/addDate.e")

    def testAddDateTime(self):
        self.compareResourceEOE("add/addDateTime.e")

    def testAddDecimal(self):
        self.compareResourceEOE("add/addDecimal.e")

    def testAddDict(self):
        self.compareResourceEOE("add/addDict.e")

    def testAddInteger(self):
        self.compareResourceEOE("add/addInteger.e")

    def testAddList(self):
        self.compareResourceEOE("add/addList.e")

    def testAddPeriod(self):
        self.compareResourceEOE("add/addPeriod.e")

    def testAddSet(self):
        self.compareResourceEOE("add/addSet.e")

    def testAddText(self):
        self.compareResourceEOE("add/addText.e")

    def testAddTime(self):
        self.compareResourceEOE("add/addTime.e")

    def testAddTuple(self):
        self.compareResourceEOE("add/addTuple.e")


