from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComposed(self):
        self.compareResourceEME("categories/composed.pec")

    def testCopyFromAscendant(self):
        self.compareResourceEME("categories/copyFromAscendant.pec")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceEME("categories/copyFromAscendantWithOverride.pec")

    def testCopyFromDescendant(self):
        self.compareResourceEME("categories/copyFromDescendant.pec")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceEME("categories/copyFromDescendantWithOverride.pec")

    def testCopyFromDocument(self):
        self.compareResourceEME("categories/copyFromDocument.pec")


