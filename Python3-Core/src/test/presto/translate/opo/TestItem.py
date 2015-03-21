from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestItem(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceOPO("item/itemDict.o")

    def testItemList(self):
        self.compareResourceOPO("item/itemList.o")

    def testItemRange(self):
        self.compareResourceOPO("item/itemRange.o")

    def testItemSet(self):
        self.compareResourceOPO("item/itemSet.o")

    def testItemText(self):
        self.compareResourceOPO("item/itemText.o")


