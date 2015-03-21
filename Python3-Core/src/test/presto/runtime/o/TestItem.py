from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestItem(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testItemDict(self):
        self.checkOutput("item/itemDict.o")

    def testItemList(self):
        self.checkOutput("item/itemList.o")

    def testItemRange(self):
        self.checkOutput("item/itemRange.o")

    def testItemSet(self):
        self.checkOutput("item/itemSet.o")

    def testItemText(self):
        self.checkOutput("item/itemText.o")


