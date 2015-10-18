from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestComment(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testComment(self):
        self.compareResourceESE("comment/comment.pec")


