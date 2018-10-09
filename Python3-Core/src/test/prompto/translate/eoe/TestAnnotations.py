from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestAnnotations(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCallback(self):
        self.compareResourceEOE("annotations/callback.pec")

    def testCategory(self):
        self.compareResourceEOE("annotations/category.pec")


