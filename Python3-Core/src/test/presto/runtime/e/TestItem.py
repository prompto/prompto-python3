from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestItem(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testItemDict(self):
        self.checkOutput("item/itemDict.e")

    def testItemList(self):
        self.checkOutput("item/itemList.e")

    def testItemRange(self):
        self.checkOutput("item/itemRange.e")

    def testItemSet(self):
        self.checkOutput("item/itemSet.e")

    def testItemText(self):
        self.checkOutput("item/itemText.e")


