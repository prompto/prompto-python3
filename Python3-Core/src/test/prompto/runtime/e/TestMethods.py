from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestMethods(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnonymous(self):
        self.checkOutput("methods/anonymous.pec")

    def testAttribute(self):
        self.checkOutput("methods/attribute.pec")

    def testDefault(self):
        self.checkOutput("methods/default.pec")

    def testE_as_e_bug(self):
        self.checkOutput("methods/e_as_e_bug.pec")

    def testExplicit(self):
        self.checkOutput("methods/explicit.pec")

    def testExpressionWith(self):
        self.checkOutput("methods/expressionWith.pec")

    def testExtended(self):
        self.checkOutput("methods/extended.pec")

    def testHomonym(self):
        self.checkOutput("methods/homonym.pec")

    def testImplicitMember(self):
        self.checkOutput("methods/implicitMember.pec")

    def testMember(self):
        self.checkOutput("methods/member.pec")

    def testMemberCall(self):
        self.checkOutput("methods/memberCall.pec")

    def testOverride(self):
        self.checkOutput("methods/override.pec")

    def testPolymorphic_abstract(self):
        self.checkOutput("methods/polymorphic_abstract.pec")

    def testPolymorphic_implicit(self):
        self.checkOutput("methods/polymorphic_implicit.pec")

    def testPolymorphic_named(self):
        self.checkOutput("methods/polymorphic_named.pec")

    def testPolymorphic_runtime(self):
        self.checkOutput("methods/polymorphic_runtime.pec")

    def testSpecified(self):
        self.checkOutput("methods/specified.pec")


