from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestItem(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceEOE("item/itemDict.pec")

    def testItemList(self):
        self.compareResourceEOE("item/itemList.pec")

    def testItemRange(self):
        self.compareResourceEOE("item/itemRange.pec")

    def testItemSet(self):
        self.compareResourceEOE("item/itemSet.pec")

    def testItemText(self):
        self.compareResourceEOE("item/itemText.pec")


