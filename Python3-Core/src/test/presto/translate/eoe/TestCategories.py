from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceEOE("categories/copyFromAscendant.e")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceEOE("categories/copyFromAscendantWithOverride.e")

    def testCopyFromDescendant(self):
        self.compareResourceEOE("categories/copyFromDescendant.e")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceEOE("categories/copyFromDescendantWithOverride.e")


