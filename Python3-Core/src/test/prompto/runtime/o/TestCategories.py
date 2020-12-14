from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestCategories(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

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

    def testEquals(self):
        self.checkOutput("categories/equals.poc")

    def testPopulateFalse(self):
        self.checkOutput("categories/populateFalse.poc")


