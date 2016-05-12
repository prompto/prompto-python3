from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestPredicate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsItem(self):
        self.compareResourceESE("predicate/containsItem.pec")

    def testEquals(self):
        self.compareResourceESE("predicate/equals.pec")

    def testGreater(self):
        self.compareResourceESE("predicate/greater.pec")

    def testInList(self):
        self.compareResourceESE("predicate/inList.pec")

    def testLesser(self):
        self.compareResourceESE("predicate/lesser.pec")

    def testNotEquals(self):
        self.compareResourceESE("predicate/notEquals.pec")

    def testPartial(self):
        self.compareResourceESE("predicate/partial.pec")

    def testRoughly(self):
        self.compareResourceESE("predicate/roughly.pec")


