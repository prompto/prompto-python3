from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestItem(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceOEO("item/itemDict.o")

    def testItemList(self):
        self.compareResourceOEO("item/itemList.o")

    def testItemRange(self):
        self.compareResourceOEO("item/itemRange.o")

    def testItemSet(self):
        self.compareResourceOEO("item/itemSet.o")

    def testItemText(self):
        self.compareResourceOEO("item/itemText.o")


