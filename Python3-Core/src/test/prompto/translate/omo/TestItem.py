from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestItem(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testItemDict(self):
        self.compareResourceOMO("item/itemDict.poc")

    def testItemList(self):
        self.compareResourceOMO("item/itemList.poc")

    def testItemRange(self):
        self.compareResourceOMO("item/itemRange.poc")

    def testItemSet(self):
        self.compareResourceOMO("item/itemSet.poc")

    def testItemText(self):
        self.compareResourceOMO("item/itemText.poc")


