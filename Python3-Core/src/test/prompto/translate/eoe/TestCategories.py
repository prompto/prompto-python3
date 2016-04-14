from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComposed(self):
        self.compareResourceEOE("categories/composed.pec")

    def testCopyFromAscendant(self):
        self.compareResourceEOE("categories/copyFromAscendant.pec")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceEOE("categories/copyFromAscendantWithOverride.pec")

    def testCopyFromDescendant(self):
        self.compareResourceEOE("categories/copyFromDescendant.pec")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceEOE("categories/copyFromDescendantWithOverride.pec")


