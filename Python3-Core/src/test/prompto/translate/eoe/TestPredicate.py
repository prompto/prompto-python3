from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestPredicate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsItem(self):
        self.compareResourceEOE("predicate/containsItem.pec")

    def testEquals(self):
        self.compareResourceEOE("predicate/equals.pec")

    def testGreater(self):
        self.compareResourceEOE("predicate/greater.pec")

    def testHasItem(self):
        self.compareResourceEOE("predicate/hasItem.pec")

    def testInList(self):
        self.compareResourceEOE("predicate/inList.pec")

    def testLesser(self):
        self.compareResourceEOE("predicate/lesser.pec")

    def testNotEquals(self):
        self.compareResourceEOE("predicate/notEquals.pec")

    def testPartial(self):
        self.compareResourceEOE("predicate/partial.pec")

    def testRoughly(self):
        self.compareResourceEOE("predicate/roughly.pec")


