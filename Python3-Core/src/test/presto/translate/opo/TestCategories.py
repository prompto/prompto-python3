from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestCategories(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceOPO("categories/copyFromAscendant.o")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceOPO("categories/copyFromAscendantWithOverride.o")

    def testCopyFromDescendant(self):
        self.compareResourceOPO("categories/copyFromDescendant.o")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceOPO("categories/copyFromDescendantWithOverride.o")


