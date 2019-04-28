from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestArrow(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSort1(self):
        self.checkOutput("arrow/sort1.poc")

    def testSort1_desc(self):
        self.checkOutput("arrow/sort1_desc.poc")

    def testSort2(self):
        self.checkOutput("arrow/sort2.poc")

    def testSort2_desc(self):
        self.checkOutput("arrow/sort2_desc.poc")


