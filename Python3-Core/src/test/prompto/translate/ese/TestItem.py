from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestItem(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceESE("item/itemDict.pec")

    def testItemList(self):
        self.compareResourceESE("item/itemList.pec")

    def testItemRange(self):
        self.compareResourceESE("item/itemRange.pec")

    def testItemSet(self):
        self.compareResourceESE("item/itemSet.pec")

    def testItemText(self):
        self.compareResourceESE("item/itemText.pec")


