from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestCategories(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testComposed(self):
        self.checkOutput("categories/composed.pec")

    def testCopyFromAscendant(self):
        self.checkOutput("categories/copyFromAscendant.pec")

    def testCopyFromAscendantWithOverride(self):
        self.checkOutput("categories/copyFromAscendantWithOverride.pec")

    def testCopyFromDescendant(self):
        self.checkOutput("categories/copyFromDescendant.pec")

    def testCopyFromDescendantWithOverride(self):
        self.checkOutput("categories/copyFromDescendantWithOverride.pec")

    def testCopyFromDocument(self):
        self.checkOutput("categories/copyFromDocument.pec")


