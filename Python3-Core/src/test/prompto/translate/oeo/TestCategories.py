from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCategories(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceOEO("categories/copyFromAscendant.poc")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceOEO("categories/copyFromAscendantWithOverride.poc")

    def testCopyFromDescendant(self):
        self.compareResourceOEO("categories/copyFromDescendant.poc")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceOEO("categories/copyFromDescendantWithOverride.poc")


