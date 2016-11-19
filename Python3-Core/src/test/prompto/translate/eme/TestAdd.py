from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestAdd(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceEME("add/addCharacter.pec")

    def testAddDate(self):
        self.compareResourceEME("add/addDate.pec")

    def testAddDateTime(self):
        self.compareResourceEME("add/addDateTime.pec")

    def testAddDecimal(self):
        self.compareResourceEME("add/addDecimal.pec")

    def testAddDecimalEnum(self):
        self.compareResourceEME("add/addDecimalEnum.pec")

    def testAddDict(self):
        self.compareResourceEME("add/addDict.pec")

    def testAddInteger(self):
        self.compareResourceEME("add/addInteger.pec")

    def testAddIntegerEnum(self):
        self.compareResourceEME("add/addIntegerEnum.pec")

    def testAddList(self):
        self.compareResourceEME("add/addList.pec")

    def testAddPeriod(self):
        self.compareResourceEME("add/addPeriod.pec")

    def testAddSet(self):
        self.compareResourceEME("add/addSet.pec")

    def testAddTextCharacter(self):
        self.compareResourceEME("add/addTextCharacter.pec")

    def testAddTextDecimal(self):
        self.compareResourceEME("add/addTextDecimal.pec")

    def testAddTextEnum(self):
        self.compareResourceEME("add/addTextEnum.pec")

    def testAddTextInteger(self):
        self.compareResourceEME("add/addTextInteger.pec")

    def testAddTextText(self):
        self.compareResourceEME("add/addTextText.pec")

    def testAddTime(self):
        self.compareResourceEME("add/addTime.pec")

    def testAddTuple(self):
        self.compareResourceEME("add/addTuple.pec")


