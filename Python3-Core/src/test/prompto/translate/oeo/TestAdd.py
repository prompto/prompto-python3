from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestAdd(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddCharacter(self):
        self.compareResourceOEO("add/addCharacter.poc")

    def testAddCss(self):
        self.compareResourceOEO("add/addCss.poc")

    def testAddDate(self):
        self.compareResourceOEO("add/addDate.poc")

    def testAddDateTime(self):
        self.compareResourceOEO("add/addDateTime.poc")

    def testAddDecimal(self):
        self.compareResourceOEO("add/addDecimal.poc")

    def testAddDict(self):
        self.compareResourceOEO("add/addDict.poc")

    def testAddDocument(self):
        self.compareResourceOEO("add/addDocument.poc")

    def testAddInteger(self):
        self.compareResourceOEO("add/addInteger.poc")

    def testAddList(self):
        self.compareResourceOEO("add/addList.poc")

    def testAddListDerived(self):
        self.compareResourceOEO("add/addListDerived.poc")

    def testAddPeriod(self):
        self.compareResourceOEO("add/addPeriod.poc")

    def testAddSet(self):
        self.compareResourceOEO("add/addSet.poc")

    def testAddSetDerived(self):
        self.compareResourceOEO("add/addSetDerived.poc")

    def testAddTextCharacter(self):
        self.compareResourceOEO("add/addTextCharacter.poc")

    def testAddTextDecimal(self):
        self.compareResourceOEO("add/addTextDecimal.poc")

    def testAddTextInteger(self):
        self.compareResourceOEO("add/addTextInteger.poc")

    def testAddTextText(self):
        self.compareResourceOEO("add/addTextText.poc")

    def testAddTime(self):
        self.compareResourceOEO("add/addTime.poc")

    def testAddTuple(self):
        self.compareResourceOEO("add/addTuple.poc")


