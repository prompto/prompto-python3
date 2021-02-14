from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCategories(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCopyFromAscendant(self):
        self.compareResourceOMO("categories/copyFromAscendant.poc")

    def testCopyFromAscendantWithOverride(self):
        self.compareResourceOMO("categories/copyFromAscendantWithOverride.poc")

    def testCopyFromDescendant(self):
        self.compareResourceOMO("categories/copyFromDescendant.poc")

    def testCopyFromDescendantWithOverride(self):
        self.compareResourceOMO("categories/copyFromDescendantWithOverride.poc")

    def testCopyFromDocument(self):
        self.compareResourceOMO("categories/copyFromDocument.poc")

    def testCopyFromStored(self):
        self.compareResourceOMO("categories/copyFromStored.poc")

    def testEquals(self):
        self.compareResourceOMO("categories/equals.poc")

    def testPopulateFalse(self):
        self.compareResourceOMO("categories/populateFalse.poc")

    def testResourceAttribute(self):
        self.compareResourceOMO("categories/resourceAttribute.poc")


