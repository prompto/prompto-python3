from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestItem(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testItemDict(self):
        self.checkOutput("item/itemDict.poc")

    def testItemList(self):
        self.checkOutput("item/itemList.poc")

    def testItemRange(self):
        self.checkOutput("item/itemRange.poc")

    def testItemSet(self):
        self.checkOutput("item/itemSet.poc")

    def testItemText(self):
        self.checkOutput("item/itemText.poc")


