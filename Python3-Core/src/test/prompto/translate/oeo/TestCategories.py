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

    def testCopyFromDocument(self):
        self.compareResourceOEO("categories/copyFromDocument.poc")

    def testCopyFromStored(self):
        self.compareResourceOEO("categories/copyFromStored.poc")

    def testEquals(self):
        self.compareResourceOEO("categories/equals.poc")

    def testPopulateFalse(self):
        self.compareResourceOEO("categories/populateFalse.poc")

    def testResourceAttribute(self):
        self.compareResourceOEO("categories/resourceAttribute.poc")


