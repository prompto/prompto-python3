from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceEPE("categories/copyFromAscendant.e")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceEPE("categories/copyFromAscendantWithOverride.e")

    def testCopyFromDescendant(self):
        self.compareResourceEPE("categories/copyFromDescendant.e")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceEPE("categories/copyFromDescendantWithOverride.e")


