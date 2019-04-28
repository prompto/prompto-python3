from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestArrow(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSort1(self):
        self.compareResourceOMO("arrow/sort1.poc")

    def testSort1_desc(self):
        self.compareResourceOMO("arrow/sort1_desc.poc")

    def testSort2(self):
        self.compareResourceOMO("arrow/sort2.poc")

    def testSort2_desc(self):
        self.compareResourceOMO("arrow/sort2_desc.poc")


