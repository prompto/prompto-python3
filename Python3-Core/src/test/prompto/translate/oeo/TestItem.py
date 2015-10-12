from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestItem(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceOEO("item/itemDict.poc")

    def testItemList(self):
        self.compareResourceOEO("item/itemList.poc")

    def testItemRange(self):
        self.compareResourceOEO("item/itemRange.poc")

    def testItemSet(self):
        self.compareResourceOEO("item/itemSet.poc")

    def testItemText(self):
        self.compareResourceOEO("item/itemText.poc")


