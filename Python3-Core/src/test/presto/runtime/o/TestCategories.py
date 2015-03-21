from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestCategories(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCopyFromAscendant(self):
        self.checkOutput("categories/copyFromAscendant.o")

    def testCopyFromAscendantWithOverride(self):
        self.checkOutput("categories/copyFromAscendantWithOverride.o")

    def testCopyFromDescendant(self):
        self.checkOutput("categories/copyFromDescendant.o")

    def testCopyFromDescendantWithOverride(self):
        self.checkOutput("categories/copyFromDescendantWithOverride.o")


