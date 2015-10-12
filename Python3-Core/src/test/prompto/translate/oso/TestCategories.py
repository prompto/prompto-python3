from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCategories(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceOSO("categories/copyFromAscendant.poc")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceOSO("categories/copyFromAscendantWithOverride.poc")

    def testCopyFromDescendant(self):
        self.compareResourceOSO("categories/copyFromDescendant.poc")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceOSO("categories/copyFromDescendantWithOverride.poc")


