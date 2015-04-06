from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestItem(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceOSO("item/itemDict.poc")

    def testItemList(self):
        self.compareResourceOSO("item/itemList.poc")

    def testItemRange(self):
        self.compareResourceOSO("item/itemRange.poc")

    def testItemSet(self):
        self.compareResourceOSO("item/itemSet.poc")

    def testItemText(self):
        self.compareResourceOSO("item/itemText.poc")


