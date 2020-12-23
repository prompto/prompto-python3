from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestArrow(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllFromList(self):
        self.compareResourceEME("arrow/hasAllFromList.pec")

    def testHasAllFromSet(self):
        self.compareResourceEME("arrow/hasAllFromSet.pec")

    def testHasAnyFromList(self):
        self.compareResourceEME("arrow/hasAnyFromList.pec")

    def testHasAnyFromSet(self):
        self.compareResourceEME("arrow/hasAnyFromSet.pec")


