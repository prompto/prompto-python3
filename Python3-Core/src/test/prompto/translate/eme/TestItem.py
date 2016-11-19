from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestItem(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceEME("item/itemDict.pec")

    def testItemList(self):
        self.compareResourceEME("item/itemList.pec")

    def testItemRange(self):
        self.compareResourceEME("item/itemRange.pec")

    def testItemSet(self):
        self.compareResourceEME("item/itemSet.pec")

    def testItemText(self):
        self.compareResourceEME("item/itemText.pec")


