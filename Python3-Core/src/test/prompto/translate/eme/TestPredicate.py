from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestPredicate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceEME("predicate/and.pec")

    def testAndError(self):
        self.compareResourceEME("predicate/andError.pec")

    def testContainsItem(self):
        self.compareResourceEME("predicate/containsItem.pec")

    def testEquals(self):
        self.compareResourceEME("predicate/equals.pec")

    def testEqualsError(self):
        self.compareResourceEME("predicate/equalsError.pec")

    def testGreater(self):
        self.compareResourceEME("predicate/greater.pec")

    def testHasItem(self):
        self.compareResourceEME("predicate/hasItem.pec")

    def testInList(self):
        self.compareResourceEME("predicate/inList.pec")

    def testLesser(self):
        self.compareResourceEME("predicate/lesser.pec")

    def testNotEquals(self):
        self.compareResourceEME("predicate/notEquals.pec")

    def testOr(self):
        self.compareResourceEME("predicate/or.pec")

    def testOrError(self):
        self.compareResourceEME("predicate/orError.pec")

    def testParenthesis(self):
        self.compareResourceEME("predicate/parenthesis.pec")

    def testParenthesisError(self):
        self.compareResourceEME("predicate/parenthesisError.pec")

    def testPartial(self):
        self.compareResourceEME("predicate/partial.pec")

    def testRoughly(self):
        self.compareResourceEME("predicate/roughly.pec")


