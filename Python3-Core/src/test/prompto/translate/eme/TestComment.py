from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestComment(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComment(self):
        self.compareResourceEME("comment/comment.pec")


