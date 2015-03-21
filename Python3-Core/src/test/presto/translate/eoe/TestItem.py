from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestItem(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceEOE("item/itemDict.e")

    def testItemList(self):
        self.compareResourceEOE("item/itemList.e")

    def testItemRange(self):
        self.compareResourceEOE("item/itemRange.e")

    def testItemSet(self):
        self.compareResourceEOE("item/itemSet.e")

    def testItemText(self):
        self.compareResourceEOE("item/itemText.e")


