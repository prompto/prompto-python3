from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestPredicate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnd(self):
        self.checkOutput("predicate/and.pec")

    def testAndError(self):
        self.checkOutput("predicate/andError.pec")

    def testContainsItem(self):
        self.checkOutput("predicate/containsItem.pec")

    def testEquals(self):
        self.checkOutput("predicate/equals.pec")

    def testEqualsError(self):
        self.checkOutput("predicate/equalsError.pec")

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

    def testOr(self):
        self.checkOutput("predicate/or.pec")

    def testOrError(self):
        self.checkOutput("predicate/orError.pec")

    def testParenthesis(self):
        self.checkOutput("predicate/parenthesis.pec")

    def testParenthesisError(self):
        self.checkOutput("predicate/parenthesisError.pec")

    def testPartial(self):
        self.checkOutput("predicate/partial.pec")

    def testRoughly(self):
        self.checkOutput("predicate/roughly.pec")


