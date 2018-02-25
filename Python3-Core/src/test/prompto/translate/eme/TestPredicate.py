from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestPredicate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsItem(self):
        self.compareResourceEME("predicate/containsItem.pec")

    def testEquals(self):
        self.compareResourceEME("predicate/equals.pec")

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

    def testPartial(self):
        self.compareResourceEME("predicate/partial.pec")

    def testRoughly(self):
        self.compareResourceEME("predicate/roughly.pec")


