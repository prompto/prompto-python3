from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestAdd(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceEOE("add/addCharacter.pec")

    def testAddDate(self):
        self.compareResourceEOE("add/addDate.pec")

    def testAddDateTime(self):
        self.compareResourceEOE("add/addDateTime.pec")

    def testAddDecimal(self):
        self.compareResourceEOE("add/addDecimal.pec")

    def testAddDecimalEnum(self):
        self.compareResourceEOE("add/addDecimalEnum.pec")

    def testAddDict(self):
        self.compareResourceEOE("add/addDict.pec")

    def testAddInteger(self):
        self.compareResourceEOE("add/addInteger.pec")

    def testAddIntegerEnum(self):
        self.compareResourceEOE("add/addIntegerEnum.pec")

    def testAddList(self):
        self.compareResourceEOE("add/addList.pec")

    def testAddPeriod(self):
        self.compareResourceEOE("add/addPeriod.pec")

    def testAddSet(self):
        self.compareResourceEOE("add/addSet.pec")

    def testAddTextCharacter(self):
        self.compareResourceEOE("add/addTextCharacter.pec")

    def testAddTextDecimal(self):
        self.compareResourceEOE("add/addTextDecimal.pec")

    def testAddTextEnum(self):
        self.compareResourceEOE("add/addTextEnum.pec")

    def testAddTextInteger(self):
        self.compareResourceEOE("add/addTextInteger.pec")

    def testAddTextText(self):
        self.compareResourceEOE("add/addTextText.pec")

    def testAddTime(self):
        self.compareResourceEOE("add/addTime.pec")

    def testAddTuple(self):
        self.compareResourceEOE("add/addTuple.pec")


