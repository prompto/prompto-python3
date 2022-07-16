from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestCategories(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAttributeConstructor(self):
        self.checkOutput("categories/attributeConstructor.poc")

    def testCopyFromAscendant(self):
        self.checkOutput("categories/copyFromAscendant.poc")

    def testCopyFromAscendantWithOverride(self):
        self.checkOutput("categories/copyFromAscendantWithOverride.poc")

    def testCopyFromDescendant(self):
        self.checkOutput("categories/copyFromDescendant.poc")

    def testCopyFromDescendantWithOverride(self):
        self.checkOutput("categories/copyFromDescendantWithOverride.poc")

    def testCopyFromDocument(self):
        self.checkOutput("categories/copyFromDocument.poc")

    def testCopyFromStored(self):
        self.checkOutput("categories/copyFromStored.poc")

    def testEmptyConstructor(self):
        self.checkOutput("categories/emptyConstructor.poc")

    def testEquals(self):
        self.checkOutput("categories/equals.poc")

    def testLiteralConstructor(self):
        self.checkOutput("categories/literalConstructor.poc")

    def testPopulateFalse(self):
        self.checkOutput("categories/populateFalse.poc")

    def testResourceAttribute(self):
        self.checkOutput("categories/resourceAttribute.poc")

    def testSynonymConstructor(self):
        self.checkOutput("categories/synonymConstructor.poc")

    def testValueConstructor(self):
        self.checkOutput("categories/valueConstructor.poc")


