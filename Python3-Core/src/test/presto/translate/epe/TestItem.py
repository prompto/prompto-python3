from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestItem(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceEPE("item/itemDict.e")

    def testItemList(self):
        self.compareResourceEPE("item/itemList.e")

    def testItemRange(self):
        self.compareResourceEPE("item/itemRange.e")

    def testItemSet(self):
        self.compareResourceEPE("item/itemSet.e")

    def testItemText(self):
        self.compareResourceEPE("item/itemText.e")


