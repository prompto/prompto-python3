from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnonymous(self):
        self.checkOutput("methods/anonymous.e")

    def testAttribute(self):
        self.checkOutput("methods/attribute.e")

    def testDefault(self):
        self.checkOutput("methods/default.e")

    def testE_as_e_bug(self):
        self.checkOutput("methods/e_as_e_bug.e")

    def testExpressionWith(self):
        self.checkOutput("methods/expressionWith.e")

    def testImplicit(self):
        self.checkOutput("methods/implicit.e")

    def testMember(self):
        self.checkOutput("methods/member.e")

    def testPolymorphic_abstract(self):
        self.checkOutput("methods/polymorphic_abstract.e")

    def testPolymorphic_implicit(self):
        self.checkOutput("methods/polymorphic_implicit.e")

    def testPolymorphic_named(self):
        self.checkOutput("methods/polymorphic_named.e")

    def testPolymorphic_runtime(self):
        self.checkOutput("methods/polymorphic_runtime.e")

    def testSpecified(self):
        self.checkOutput("methods/specified.e")


