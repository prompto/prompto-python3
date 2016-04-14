from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComposed(self):
        self.compareResourceESE("categories/composed.pec")

    def testCopyFromAscendant(self):
        self.compareResourceESE("categories/copyFromAscendant.pec")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceESE("categories/copyFromAscendantWithOverride.pec")

    def testCopyFromDescendant(self):
        self.compareResourceESE("categories/copyFromDescendant.pec")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceESE("categories/copyFromDescendantWithOverride.pec")


