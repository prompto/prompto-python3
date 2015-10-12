from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestItem(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testItemDict(self):
        self.checkOutput("item/itemDict.pec")

    def testItemList(self):
        self.checkOutput("item/itemList.pec")

    def testItemRange(self):
        self.checkOutput("item/itemRange.pec")

    def testItemSet(self):
        self.checkOutput("item/itemSet.pec")

    def testItemText(self):
        self.checkOutput("item/itemText.pec")


