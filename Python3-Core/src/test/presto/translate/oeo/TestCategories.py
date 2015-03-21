from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestCategories(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceOEO("categories/copyFromAscendant.o")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceOEO("categories/copyFromAscendantWithOverride.o")

    def testCopyFromDescendant(self):
        self.compareResourceOEO("categories/copyFromDescendant.o")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceOEO("categories/copyFromDescendantWithOverride.o")


