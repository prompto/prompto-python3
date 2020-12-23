from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestArrow(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllFromList(self):
        self.compareResourceEOE("arrow/hasAllFromList.pec")

    def testHasAllFromSet(self):
        self.compareResourceEOE("arrow/hasAllFromSet.pec")

    def testHasAnyFromList(self):
        self.compareResourceEOE("arrow/hasAnyFromList.pec")

    def testHasAnyFromSet(self):
        self.compareResourceEOE("arrow/hasAnyFromSet.pec")


