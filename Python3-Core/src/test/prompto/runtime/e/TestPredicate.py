from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestPredicate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testContainsItem(self):
        self.checkOutput("predicate/containsItem.pec")

    def testEquals(self):
        self.checkOutput("predicate/equals.pec")

    def testGreater(self):
        self.checkOutput("predicate/greater.pec")

    def testHasItem(self):
        self.checkOutput("predicate/hasItem.pec")

    def testInList(self):
        self.checkOutput("predicate/inList.pec")

    def testLesser(self):
        self.checkOutput("predicate/lesser.pec")

    def testNotEquals(self):
        self.checkOutput("predicate/notEquals.pec")

    def testPartial(self):
        self.checkOutput("predicate/partial.pec")

    def testRoughly(self):
        self.checkOutput("predicate/roughly.pec")


