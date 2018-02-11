from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestFilter(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testFilterFromCursor(self):
        self.compareResourceEME("filter/filterFromCursor.pec")

    def testFilterFromList(self):
        self.compareResourceEME("filter/filterFromList.pec")

    def testFilterFromSet(self):
        self.compareResourceEME("filter/filterFromSet.pec")


